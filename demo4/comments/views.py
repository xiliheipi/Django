from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.views.generic import View
from django.http import HttpResponse
from gametest.models import HeroIntro
from .models import Comment
# Create your views here.

class AddComment(View):
    def post(self,request,id):
        hero = get_object_or_404(HeroIntro,pk = id)

        name = request.POST.get('Name')
        email = request.POST.get('Email')
        subject = request.POST.get('Subject')
        content = request.POST.get('Message')

        c = Comment()
        c.username = name
        c.email = email
        c.subject = subject
        c.content = content
        c.heroIntro = hero
        c.save()
        return redirect(reverse('gametest:single',args=(id,)))









