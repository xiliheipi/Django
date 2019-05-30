from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect,get_object_or_404,reverse
from .models import *
from django.views.generic import View
from django.core.mail import send_mass_mail,send_mail
from django.conf import settings
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



class Contact(View):
    def get(self,request):
        return render(request, 'contact.html')

    def post(self,request):
        m = MessageInfo()
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        subject = request.POST.get('subject')
        send_mail('建议', subject, settings.DEFAULT_FROM_EMAIL, ['826918436@qq.com'])

        m.username = username
        m.email = email
        m.phone = phone
        m.city = city
        m.subject = subject
        m.save()

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

        for cate in hero.category.all():
            print(cate,type(cate.title))
        return render(request, 'single.html', locals())


# 英雄分类
def Cate(request,id):
    cate = get_object_or_404(Category,pk = id)

    catehero = cate.herointro_set.all()

    return render(request, 'category.html', locals())




def Detail(request):

    return render(request,'detail.html')





