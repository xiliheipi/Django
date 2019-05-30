from django import template
from ..models import Ads,HeroIntro


register = template.Library()

'''
过滤器最多两个参数
标签可以有任意多个参数

'''

# 轮播英雄图
@register.simple_tag
def getads():
    ads = Ads.objects.all()
    # for a in ads:
    #     print(a.herointro_set.first().id)
    # print(ads[0].herointro_set.all().first().id,'+++++++++')
    return ads


# 英雄
@register.simple_tag
def getheros():
    hero = HeroIntro.objects.all()
    print(len(hero),'AAAAA')
    return hero


#  阅读量最多的英雄
@register.simple_tag
def getlateheros(num = 5):
         # -create_time[:num]  时间倒叙
    return HeroIntro.objects.all().order_by('-views')[:num]


# 获得最新文章  也就是最后发布的文章
@register.simple_tag
def getlatesthero(num = 5):
         # -create_time[:num]  时间倒叙
    return HeroIntro.objects.all().order_by('-create_time')[:num]






# 归档
@register.simple_tag
def getarchives(num = 5):
    result =  HeroIntro.objects.dates("create_time",'month',order="DESC")[:num]
    print(result)
    return result








