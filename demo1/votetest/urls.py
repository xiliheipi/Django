
from django.conf.urls import url
from . import views


app_name = 'votetest'


urlpatterns =[

    url(r'^index/$', views.index,name='index'),
    url(r'^list/(\d+)/$', views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),



]






