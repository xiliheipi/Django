from django.conf.urls import url
from . import views

app_name = 'gametest'

urlpatterns=[

    url(r'^single/(\d+)/$',views.Single,name='single'),

    url(r'^index/$',views.Index,name='index'),
    url(r'^about/$',views.About,name='about'),
    url(r'^games/$',views.Games,name='games'),
    url(r'^news/$',views.News,name='news'),
    url(r'^contact/$',views.Contact.as_view(),name='contact'),

    # 英雄分类
    url(r'cate/(\d+)/$',views.Cate,name = 'cate'),
    #全英雄
    url(r'^detail/$',views.Detail,name = 'detail'),

]



