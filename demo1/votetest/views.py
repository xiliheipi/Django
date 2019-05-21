from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.template import loader
from .models import Headline,Option,User
from .util import checklogin
from django.http import HttpResponseRedirect
# Create your views here.



def logout(request):

    del request.session['username']
    return redirect(reverse('votetest:login'))

def login(request):
    if request.method == 'GET':
        return render(request,'votetest/login.html')
    else:
        username = request.POST.get("username")
        userpwd = request.POST.get('userpwd')
        try:
            username = User.objects.get(name=username,pwd=userpwd)
            res = redirect(reverse('votetest:index'))
            request.session['username'] = username
            return res
        except:
            return render(request,'votetest/login.html',{'error':'用户名错误'})



def register(request):
    if request.method == 'GET':
        return render(request, 'votetest/register.html')
    else:
        username = request.POST.get('username')
        userpwd = request.POST.get('password')
        try:
            username = User.objects.get(name = username)
            return render(request, 'votetest/register.html', {'error': '账户或密码存在'})
        except:
            b1 = User()
            b1.name = username
            b1.pwd = userpwd
            b1.save()
            return render(request,'votetest/register.html',{'error': '注册成功！'})



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


