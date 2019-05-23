from django import template
from ..models import Article,Category,Tag



register = template.Library()

'''
过滤器最多两个参数
标签可以有任意多个参数

'''



@register.filter(name='mylower')
def mylower(value):
    return value.lower()



@register.filter(name='myslice')
def myslice(value,length):
    result = value[:length]
    print(result)
    return  result




# 得到所有的分类
@register.simple_tag(name='getcategorys')
def getcategorys():
    return Category.objects.all()


# 获得最新文章  也就是最后发布的文章
@register.simple_tag
def getlatestarticles(num = 3):
         # -create_time[:num]  时间倒叙
    return Article.objects.all().order_by('-create_time')[:num]



# 归档
@register.simple_tag
def getarchives(num = 3):
    result =  Article.objects.dates("create_time",'month',order="DESC")[:num]
    print(result)
    return result


# 云标签
@register.simple_tag
def gettags():
    return Tag.objects.all()



