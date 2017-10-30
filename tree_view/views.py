from django.shortcuts import render
from .models import New
from . import APP_LABEL


def index(request):
    return render(request, APP_LABEL + '/index.html')


def embedding(request):
    # 最新5件のニュースをデータベースから取得
    obj_latest_5 = New.objects.order_by('-date')[:5]
    context = {'latest_news_list': obj_latest_5}
    if len(context['latest_news_list']) == 0:
        return render(request, APP_LABEL + '/test_embedding.html')
    else:
        return render(request, APP_LABEL + '/test_embedding.html', context)
