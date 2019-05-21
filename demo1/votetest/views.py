from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.template import loader
from .models import Headline,Option,User,MyUser
from .util import checklogin
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as lgi,logout as lgo
# 引入表单类
from .forms import LoginForm,RegisterForm


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
        print(username,pwd)
        user = authenticate(request,username = username,password = pwd)
        if user :
            print(user)

            lgi(request,user)
            return redirect(reverse('votetest:index'))
        else:
            return render(request,'votetest/login.html',{'error':'用户名或者密码错误'})


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
    #













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
        print(username,pwd)
        #在数据库创建对象
        MyUser.objects.create_user(username = username, password=pwd,url = 'http://xs8269.com')
        return redirect(reverse('votetest:login'))









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


