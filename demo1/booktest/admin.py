from django.contrib import admin
from .models import HeroInfo,BookInfo
# Register your models here.

# #   关联注册
# class HeroInfoline(admin.StackedInline):
#     model = HeroInfo
#     extra = 1




class BookInfoAdmin(admin.ModelAdmin):
    # list_display 显示字段，可以点击列头进行排序
    list_display = ['title','pub_date']
    # list_filter :过滤字段，过滤框会出现在右侧
    list_filter = ['title','pub_date']
    #search_fields:搜索字段，搜索框会出现在上侧
    search_fields = ['title','pub_date']
    #list_per_page:分页，分页框会出现在下侧（1，就是一页显示一个）
    list_per_page = 1




admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)







