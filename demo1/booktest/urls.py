from django.conf.urls import url
from . import views

urlpatterns =[
    # ^以什么什么开头，$以什么什么结尾
    url(r'^index/$', views.index),
    url(r'^list/$', views.list),
    url(r'^detail/(\d+)/$',views.detail),


]



