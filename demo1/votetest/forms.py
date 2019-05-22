# 使用Django form 类，自动生成表单元素

from django import forms
from .models import MyUser

class LoginForm(forms.Form):
    '''
    手动构造登录表单  麻烦
    '''

    username = forms.CharField(min_length=5,max_length=10,required=True,widget=forms.TextInput,error_messages={'min_length':'不能少于5个字符','max_length':'不能大于10个字符','require':'必填项'})
    password = forms.CharField(min_length=5,max_length=10,required=True,widget=forms.PasswordInput)




class RegisterForm(forms.ModelForm):
    """
    由模型类自动生成表单
    """
    class Meta():
        model = MyUser
        fields = ['url','username']






