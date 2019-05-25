from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import Headline,Option,User,MyUser
from .util import checklogin
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as lgi,logout as lgo
# 引入表单类
from .forms import LoginForm,RegisterForm
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings

from PIL import Image,ImageDraw,ImageFont
import io,random
# 引入序列化加密并且有效期信息
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired


# Create your views here.



def logout(request):
    # # 自己写的第一种方法
    # del request.session['username']
    # return redirect(reverse('votetest:login'))

    # Django自带方法
    res = redirect(reverse('votetest:login'))
    lgo(request)
    return res

def login(request):

    # 自己的第一种方法
    # if request.method == 'GET':
    #     return render(request,'votetest/login.html')
    # else:
    #     username = request.POST.get("username")
    #     userpwd = request.POST.get('userpwd')
    #     try:
    #         user = User.objects.get(name=username,pwd=userpwd)
    #         res = redirect(reverse('votetest:index'))
    #         request.session['username'] = user.name
    #         return res
    #     except:
    #         return render(request,'votetest/login.html',{'error':'用户名错误'})


    #
    #   第二种方法，使用Django自带用户系统
    if request.method == "GET":
        return render(request,'votetest/login.html')

    else:
        username = request.POST.get('username')

        pwd = request.POST.get('userpwd')
        verifycode = request.POST.get('verify')

        # 如果在session中的验证码相等
        if verifycode == request.session.get('verifycode'):

            # user = authenticate(request,username = username,password = pwd)
            user = get_object_or_404(MyUser,username = username)

            # 核对用户输入密码和数据库密码（数据库密码加密，只能用用这种方式对比）

            print(user.is_active)
            if not user.is_active:
                return render(request,'votetest/login.html',{'error':'用户尚未激活'})
            else:
                check = user.check_password(pwd)
                if check:
                    lgi(request,user)
                    return redirect(reverse('votetest:index'))

                else:
                    return render(request, 'votetest/login.html', {'error': '用户名或者密码错误'})

        else:
            return render(request,'votetest/login.html',{'error':'验证码错误'})





        # # 第三种方法
        # #使用自动生成表单post
        # if request.method == 'GET':
        #     lf = LoginForm()
        #     rf = RegisterForm()
        #     return render(request,'votetest/login.html',{'lf':lf,'rf':rf})
        #
        # else:
        #     lf = LoginForm(request.POST)
        #     #如果 lf 正确有效
        #     if lf.is_valid():
        #         username = lf.cleaned_data['username']
        #         pwd = lf.cleaned_data['password']
        #         user = authenticate(request,username = username,password = pwd)
        #         if user:
        #             print(user)
        #             lgi(request,user)
        #             return redirect(reverse('votetest:index'))
        #         else:
        #             return render(request,'votetest/login.html',{'error':'用户名或密码错误'})

def register(request):
    # 自己写的第一种方法
    # if request.method == 'GET':
    #     return render(request, 'votetest/login.html')
    # else:
    #     username = request.POST.get('username')
    #     userpwd = request.POST.get('password')
    #     try:
    #         username = User.objects.get(name = username)
    #         return render(request, 'votetest/login.html', {'error': '账户或密码存在'})
    #     except:
    #         b1 = User()
    #         b1.name = username
    #         b1.pwd = userpwd
    #         b1.save()
    #         return render(request,'votetest/login.html',{'error': '注册成功！'})

#   第二种方法  Django 自带方法
    if request.method == "POST":
        username = request.POST.get('username_regi')
        pwd = request.POST.get('password_regi')
        email = request.POST.get('email')
        #在数据库创建对象
        user = MyUser.objects.create_user(username = username, password=pwd,url = 'http://xs8269.com')

        # 注册账户后，默认为非激活状态
        user.is_active = False
        user.save()
        # 第一种方法，只发送一个邮件
        # send_mail('点击激活', url, settings.DEFAULT_FROM_EMAIL,[email])


        #为了防止非人为激活用户，需要将激活地址加密
        #带有有效期的序列化
        # 得到序列化工具，默认有效期为1小时
        serutil = Serializer(settings.SECRET_KEY)
        #使用工具对字典对象序列化
        result = serutil.dumps({'userid':user.id}).decode('utf-8')
        print(result,type(result))
        # 不加decode('utf-8') 类型是 <class 'bytes'>
        # 加decode('utf-8')  类型是 <class 'str' >


        # 给邮箱发送HTMl的超链接，点开直接可以访问页面
        mail = EmailMultiAlternatives('点击激活用户',"<a href = 'http://127.0.0.1:8000/votetest/active/%s/'>点击激活</a>"%(result,),settings.DEFAULT_FROM_EMAIL,[email])
        mail.content_subtype = "html"
        mail.send()

        return render(request,'votetest/login.html',{'error':'请在一小时内激活'})




def active(request,info):
    # 序列化 并且有效期默认为1小时
    serutil = Serializer(settings.SECRET_KEY)

    try:
        obj = serutil.loads(info)
        print(obj['userid'])
        id = obj['userid']

        user = get_object_or_404(MyUser, pk=id)
        user.is_active = True
        user.save()
        return redirect(reverse('votetest:login'))


    except SignatureExpired as e:
        return HttpResponse('过期了')





def verify(request):
    # try:
    #     with open('1.png', 'wb') as f:
    #         return HttpResponse(f.readable())
    # except Exception as e:
    #     print(e)
    #     return HttpResponse("出错了")

    # 每次请求验证码，需要使用pillow构造出图像，返回
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 35
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        # 随机取得位置
        xy = (random.randrange(0, width), random.randrange(0, heigth))
        # 随机取得颜色
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        # 填充
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    print(rand_str)
    # 构造字体对象
    font = ImageFont.truetype('cambriab.ttf', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)


    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')



def checkuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        print(username)
        result=MyUser.objects.filter(username = username).first()
        # result=MyUser.objects.all()
        print(result)
        if result:
            return JsonResponse({'issuccess':True})

        else:
            return JsonResponse({'issuccess':False})








# 更改密码
def changepwd(request):
    if request.method == "POST":
        username = request.POST.get('')

    else:
        return render(request,'votetest/changepwd.html',{'error':'用户名或者密码错误'})




























@checklogin
# 投票主页面
def index(request):

    allHeadline = Headline.objects.all()
    return render(request,'votetest/index.html',{'allHeadline': allHeadline})

@checklogin
# 选项列表页
def list(request,id):
    headline = None
    try:
        headline = Headline.objects.get(pk = id)
        print(headline)
    except Exception as e:
        return HttpResponse('没有选项信息')
    if request.method == 'GET':
        return render(request,'votetest/list.html',{'headline':headline})
    elif request.method == "POST":
        optionid = request.POST['button']
        option1 = Option.objects.get(pk=optionid)
        option1.poll +=1
        option1.save()

    return HttpResponseRedirect('/votetest/detail/%s' %id)

@checklogin
#  展示详情结果页
def detail(request,id):
    print(id)
    headline = Headline.objects.get(pk = id)
    # 通过投票名找选项
    name = headline.option_set.all()
# <QuerySet [<Option: 邢帅,10,邢帅和吴彦祖谁比较帅？>,
# <Option: 吴彦祖,1,邢帅和吴彦祖谁比较帅？>]>
    temp = loader.get_template('votetest/detail.html')
    result = temp.render({'name':name,'headline':headline})
    return HttpResponse(result)






