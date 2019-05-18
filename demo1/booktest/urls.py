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

    # 删除角色
    url(r'^deletehero/(\d+)/$', views.deletehero,name = 'deletehero'),
    # 添加角色
    url(r'^addhero/(\d+)/$',views.addhero,name = 'addhero'),
#     编辑角色
    url(r'^edithero/(\d+)/$',views.edithero, name = 'edithero'),

    # 删除书
    url(r'^deletebook/(\d+)/$', views.deletebook,name = 'deletebook'),
    #添加书
    url(r'^addbook/$',views.addbook, name = 'addbook'),
    #编辑书
    url(r'^edtibook/(\d+)/$',views.edtibook,name = 'edtibook'),













]



