from . import views
from django.conf.urls import url
from . import feed

app_name = 'blog'

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'archives/(\d+)/(\d+)$',views.archives,name = 'archives'),
    # 分类路由
    url(r'category/(\d+)/$',views.category,name = 'category'),

    # 标签云  路由
    url(r'tag/(\d+)/$',views.tag,name = 'tag'),
    # rss 订阅路由
    url(r'rss/$',feed.BlogFeed(),name = 'rss'),

    url(r'contactus/$',views.contactus,name = 'contactus'),




]





