from django.db import models

# Create your models here.
# 创建模型

# 一个表对应一个模型类
class BookInfo(models.Model):
    #每一个字段对应 表中的一列
    title = models.CharField(max_length=30, verbose_name='书名')
    #auto_now_add = Ture 意味着默认时间为 该行插入时间
    pub_date = models.DateTimeField(auto_now_add = True,verbose_name='发行时间')

    # 显示成中文
    def __str__(self):
        return self.title

Gender = (('man','男'),('woman','女'))

class HeroInfo(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    # bool 类型性别  默认值为 True 代表男
    # gender = models.BooleanField(default=True)
    gender = models.CharField(max_length=10,choices=Gender,verbose_name='性别')

    #null = True 代表该列可以为空
    skill = models.CharField(max_length=50,null=True,verbose_name='技能')
    # ForeignKey 表名和BookInfo 为多一关系
    #book 的类型 BookInfo(对象)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE, verbose_name='书')

    # 显示成中文
    def __str__(self):
        return self.name




# --------------------封装的方法------------------------------

# class ManageExt(models.Manager):
#     def createstmodel2(self, _title):
#         t = self.model()
#         t.title = _title
#         t.save()
#
#     def deletetestmodel2(self, _pk):
#         self.get(pk = _pk).delete()
#
#
# class TestModel(models.Model):
#     title = models.CharField(max_length=20)
#     # 添加字段 字段为模型管理器
#     objects = models.Manager()
#     #应为 manage2 继承了 manage 并且扩展了功能
#     manage2 = ManageExt()
#     #在模型类中封装方法，减少重复代码的编写
#     @classmethod
#     def createtestmodel(cls,_title):
#         t = cls(title = _title)
#         t.title = _title
#         t.save()

