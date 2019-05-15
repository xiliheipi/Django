from django.shortcuts import render
from django.http import HttpResponse
# 加载模板
from django.template import loader
from .models import HeroInfo,BookInfo

# Create your views here.

# MVT 中的 V 可以是视图函数，也可以是视图类

# 视图接口

# 主页面
def index(request):

    # 1 获取模板
    template = loader.get_template('booktest/index.html')
    # 2 构造参数字典
    contex = {'username':'heipi'}
    # 3 使用模板渲染动态数据
    result = template.render(contex)

#     返回
    return HttpResponse(result)

#  列表显示书籍
def list(request):
    # 查所有书籍
    allbook = BookInfo.objects.all()
    print(allbook)
    # 1 获取模板
    temp1 = loader.get_template('booktest/list.html')
    # 2 构造参数字典,使用模板渲染动态数据
    result = temp1.render({'allbook': allbook})

    return HttpResponse(result)

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
    # 1 获取模板
    temp1 = loader.get_template('booktest/detail.html')
    # 2 构造参数字典,使用模板渲染动态数据
    result = temp1.render({'book':book})
    return HttpResponse(result)

