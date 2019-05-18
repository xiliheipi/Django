from django.shortcuts import render
from django.http import HttpResponse
# 加载模板
from django.template import loader
from .models import Headline,Option

from django.http import HttpResponseRedirect
# Create your views here.

# 投票主页面
def index(request):

    allHeadline = Headline.objects.all()
    return render(request,'votetest/index.html',{'allHeadline': allHeadline})


# 选项列表页
def list(request,id):
    headline = None
    try:
        headline = Headline.objects.get(pk = id)
        print(headline)
    except Exception as e:
        return HttpResponse('没有选项信息')
    if request.method == 'GET':
        return render(request,'votetest/list.html',{'headline':headline})
    elif request.method == "POST":
        optionid = request.POST['button']
        option1 = Option.objects.get(pk=optionid)
        option1.poll +=1
        option1.save()

    return HttpResponseRedirect('/votetest/detail/%s' %id)


#  展示详情结果页
def detail(request,id):
    print(id)
    headline = Headline.objects.get(pk = id)
    name = headline.option_set.all()
# <QuerySet [<Option: 邢帅,10,邢帅和吴彦祖谁比较帅？>,
# <Option: 吴彦祖,1,邢帅和吴彦祖谁比较帅？>]>
    temp = loader.get_template('votetest/detail.html')
    result = temp.render({'name':name,'headline':headline})
    return HttpResponse(result)


