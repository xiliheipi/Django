from django.db import models
from tinymce.models import HTMLField
from gametest.models import *
# Create your models here.


# 文章评价表
class Comment(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    url = models.URLField(blank=True,null = True)
    # 评论主题
    subject = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    heroIntro = models.ForeignKey(HeroIntro, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username

    class Meta():
        verbose_name = '评论'
        verbose_name_plural = verbose_name







