from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

# 分类信息表
class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name ='分类'
        verbose_name_plural = verbose_name


# 标签类
class Tag(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "标签"
        verbose_name_plural = verbose_name


# 文章类
class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # 评论数 类型（正整数）
    views = models.PositiveIntegerField(default=0)
    # 文章类型
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    auther = models.ForeignKey(User,models.CASCADE)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class MessageInfo(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    subject = models.CharField(max_length=50)
    # 非Django原生类型
    info = HTMLField()









