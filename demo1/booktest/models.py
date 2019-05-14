from django.db import models

# Create your models here.
# 创建模型

# 一个表对应一个模型类
class BookInfo(models.Model):
    #每一个字段对应 表中的一列
    title = models.CharField(max_length=30)
    #auto_now_add = Ture 意味着默认时间为 该行插入时间
    pub_date = models.DateTimeField(auto_now_add=True)

    # 显示成中文
    def __str__(self):
        return self.title



class HeroInfo(models.Model):
    name = models.CharField(max_length=30)
    # bool 类型性别  默认值为 True 代表男
    gender = models.BooleanField(default=True)
    #null = True 代表该列可以为空
    skill = models.CharField(max_length=50,null=True)
    # ForeignKey 表名和BookInfo 为多一关系
    #book 的类型 BookInfo(对象)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    # 显示成中文
    def __str__(self):
        return self.name



