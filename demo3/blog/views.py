from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article,Category,Tag
# 分页模块 Paginator  分页器
from django.core.paginator import Paginator
import markdown

# Create your views here.




def index(request):

    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum == None else pagenum
    # 得到所有文章         根据访问量降序排列
    articles = Article.objects.all().order_by('-views')
    paginator = Paginator(articles,1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)


    return render(request,'index.html',{'page':page})




def detail(request, id):
    # django自带的出现处理错误的方法
    article = get_object_or_404(Article,pk = id)

    # 阅读数 每点一次加1
    article.views += 1
    article.save()


    #  使用MarkDown处理body 将markdown语法转换成html标签

    # # # 第一种使用 针对需要处理的  article.body 将markdown转为html
    # article.body = markdown.markdown(article.body,extensions = [
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    #     'markdown.extensions.toc',
    # ])
    # #
    mk = markdown.Markdown(extensions=[
              'markdown.extensions.extra',
              'markdown.extensions.codehilite',
              'markdown.extensions.toc',
    ])



    article.body = mk.convert(article.body)
    # 将markdown 中的目录赋予article对象
    article.toc = mk.toc

    # cf = CommentForm()

    return render(request,'single.html',locals())



def archives(request,year,month):

    # 属性__比较类型 =
    articles = Article.objects.filter(create_time__year = year,create_time__month = month)

    paginator = Paginator(articles,1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(1)

    return render(request,'index.html',{'page':page})


 # 分类路由
def category(request,id):
    articles = get_object_or_404(Category,pk = id).article_set.all()

    paginator = Paginator(articles,1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(1)

    return render(request,'index.html',{'page':page})


# 标签云 路由
def tag(request,id):
    articles = get_object_or_404(Tag,pk = id).article_set.all()

    paginator = Paginator(articles,1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(1)

    return render(request,'index.html',{'page':page})

def contactus(request):
    return render(request,'contact.html')



