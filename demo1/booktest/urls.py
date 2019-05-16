from django.conf.urls import url
from . import views


# 去除硬编码
# 给应用添加命名空间
app_name = 'booktest'


urlpatterns =[
    # ^以什么什么开头，$以什么什么结尾
    url(r'^index/$', views.index,name='index'),
    url(r'^list/$', views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),

    # 删除英雄
    url(r'^deletehero/(\d+)/$', views.deletehero,name = 'deletehero'),
    # 添加英雄
    url(r'^addhero/(\d+)/$',views.addhero,name = 'addhero'),


    # 删除书 的路由
    url(r'^deletebook/(\d+)/$', views.deletebook,name = 'deletebook'),
    #添加书 的路由
    url(r'^addbook/$',views.addbook, name = 'addbook'),


    #更改书名
    url(r'^updatebook/$',views.updatebook,name = 'updatebook'),



]



