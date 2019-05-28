from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect



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





def Single(request):
    return render(request,'single.html')
