from django.db import models
from django.contrib.auth.models import User
# Create your models here.




# 标签   （坦克，物理输出，法术输出，控制）
class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name ='英雄类型分类'
        verbose_name_plural = verbose_name



# 英雄位置分类表  （上单，打野，射手，法师，辅助）
class Postion(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "英雄位置标签"
        verbose_name_plural = verbose_name


# 文章英雄简介类   （英雄的介绍）
class HeroIntro(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # 评论数 类型（正整数）
    views = models.PositiveIntegerField(default=0)
    # 英雄类型分类
    category = models.ManyToManyField(Category)
    # 英雄位置类型
    postion = models.ManyToManyField(Postion)
    author = models.ForeignKey(User,models.CASCADE)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '英雄简介'
        verbose_name_plural = verbose_name
