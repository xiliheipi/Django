from django.db import models

# Create your models here.

# 标题（也就是书）
class Headline(models.Model):
    title = models.CharField(max_length=20,verbose_name='标题名')

    def __str__(self):
        return self.title



# 选项（也就是书中的角色）
class Option(models.Model):
    # 名字
    name = models.CharField(max_length=50,verbose_name= '名字')
    # 票数
    poll = models.IntegerField(verbose_name='票数')
    # 外键
    headline = models.ForeignKey(Headline,on_delete=models.CASCADE, verbose_name='标题')

    def __str__(self):
        return ('%s,%s,%s')%(self.name,self.poll,self.headline)