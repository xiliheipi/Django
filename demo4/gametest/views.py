from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect,get_object_or_404
from .models import *
# 分页器
from django.core.paginator import Paginator

def Index(request):
    return render(request,'index.html')


def About(request):
    return render(request,'about.html')



def Games(request):
    return render(request,'games.html')




def News(request):
    return render(request,'news.html')




def Contact(request):
    return render(request, 'contact.html')





def Single(request,id):

    # 翻页功能
    id = int(id)
    herolist = HeroIntro.objects.all()
    print(id)
    if id < 1:
        id = len(herolist)
        hero = get_object_or_404(HeroIntro,pk = id)
        hero.views += 1
        hero.save()
        return     render(request, 'single.html', locals())
    elif id > len(herolist):
        id = 1
        hero = get_object_or_404(HeroIntro, pk=id)
        hero.views += 1
        hero.save()
        return render(request, 'single.html', locals())
    else:
        hero = get_object_or_404(HeroIntro, pk=id)
        hero.views += 1
        hero.save()
        return render(request, 'single.html', locals())














