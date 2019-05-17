from django.shortcuts import render
from django.http import HttpResponse
# 加载模板
from django.template import loader
from .models import HeroInfo,BookInfo

from django.http import HttpResponseRedirect

# Create your views here.

# MVT 中的 V 可以是视图函数，也可以是视图类

# 视图接口

# 主页面
def index(request):
    # # 1 获取模板
    # template = loader.get_template('booktest/index.html')
    # # 2 构造参数字典
    # contex = {'username': 'heipi'}
    # # 3 使用模板渲染动态数据
    # result = template.render(contex)
    # #     返回
    # return HttpResponse(result)
#     新写法
    context = {'username':'黑皮'}
    return render(request,'booktest/index.html',context)






#  列表显示书籍
def list(request):
    # # 查所有书籍
    allbook = BookInfo.objects.all()
    # print(allbook)
    # # 1 获取模板
    # temp1 = loader.get_template('booktest/list.html')
    # # 2 构造参数字典,使用模板渲染动态数据
    # result = temp1.render()
    #
    # return HttpResponse(result)
    return render(request,'booktest/list.html',{'allbook': allbook})





# 显示 点击的书  中的英雄名字和技能
def detail(request,id):
    print(id)
#       id 代表书的主键,也就是英雄的外键  pk
    book = None
    try:
        # 通过id找到对应书
        book = BookInfo.objects.get(pk=id)
        print(book)
    except Exception as e:
        return HttpResponse('没有书籍信息')
#     # 1 获取模板
#     temp1 = loader.get_template('booktest/detail.html')
#     # 2 构造参数字典,使用模板渲染动态数据
#     result = temp1.render({'book':book})
#     return HttpResponse(result)
    return render(request,'booktest/detail.html',{'book':book})


# 删除角色，返回detail 和 书的id
def deletehero(request,id):
    hero = HeroInfo.objects.get(pk = id)
    bookid=hero.book.id
    hero.delete()

    return HttpResponseRedirect('/booktest/detail/%s/' %bookid)


# 删除书,返回书的list
def deletebook(request,id):
    BookInfo.objects.get(pk = id).delete()
    return HttpResponseRedirect('/booktest/list/')

# 添加书
def addbook(request):
    if request.method =='GET':
        return render(request, 'booktest/addbook.html', {})
    elif request.method == 'POST':
        book = BookInfo()
        book.title = request.POST['title']
        book.pub_date = request.POST['pub_date']
        book.save()

        return HttpResponseRedirect('/booktest/list')



# 添加角色
def addhero(request,id):
    if request.method == 'GET':
        return render(request, 'booktest/addhero.html',{'bookid':id})

    elif request.method == 'POST':
        book = BookInfo.objects.get(pk = id)

        hero = HeroInfo()
        hero.name = request.POST['username']
        hero.gender = request.POST['sex']
        hero.skill = request.POST['skill']
        hero.book = book
        hero.save()


        return HttpResponseRedirect('/booktest/detail/%s/'%(id,))

# 编辑书籍
def edtibook(request,id):
    book = BookInfo.objects.get(pk = id)

    if request.method == 'GET':
        return render(request,'booktest/editbook.html',{'book':book})

    elif request.method == 'POST':
        book.title = request.POST['title']
        book.pub_date = request.POST['pub_date']
        book.save()

        return HttpResponseRedirect('/booktest/list/')




# 编辑英雄
def edithero(request,id):
    hero = HeroInfo.objects.get(pk = id)

    if request.method == 'GET':

        return render(request, 'booktest/edithero.html', {'hero': hero})

    elif request.method == 'POST':

        hero.name = request.POST['username']
        hero.gender = request.POST['sex']
        hero.skill = request.POST['skill']
        hero.save()

        return HttpResponseRedirect('/booktest/detail/%s/'%(hero.book.id,))






