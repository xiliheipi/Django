from . import views
from django.conf.urls import url
app_name = 'blog'

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),

]





