from django.conf.urls import url
from . import views

app_name = 'gametest'

urlpatterns=[
    url(r'^index/$',views.Index,name='index'),
    url(r'^about/$',views.About,name='about'),
    url(r'^games/$',views.Games,name='games'),
    url(r'^news/$',views.News,name='news'),
    url(r'^single/$',views.Single,name='single'),
    url(r'contact/$',views.Contact,name = 'contact'),
]



