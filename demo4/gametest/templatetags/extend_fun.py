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





