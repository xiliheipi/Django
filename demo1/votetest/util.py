from django.shortcuts import redirect,reverse

# 调用流程
# 将index函数作为fun实参传入checklogin 并且执行执行check()

def checklogin(fun):


    #自己写的第一种方法
    # def check(request,*args):
    #     #在 cookies找用户
    #     #un = request.COOKIES.get('username')
    #
    #     #在session中取
    #     un = request.session.get('username')
    #     if un:
    #         return fun(request,*args)
    #     else:
    #         #重定向(如果session没有用户登录信息，重定向到登录页面)
    #         return redirect(reverse('votetest:login'))
    # return check

    def check(request,*args):
        if request.user and request.user.is_authenticated:
            return fun(request,*args)
        else:
            return redirect(reverse('votetest:login'))

    return check






