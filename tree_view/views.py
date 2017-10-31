from django.shortcuts import render
from .models import New
from . import APP_LABEL


def embedding(request):
    # 最新5件のニュースをデータベースから取得
    obj_latest_5 = New.objects.order_by('-date')[:5]
    context = {'latest_news_list': obj_latest_5}
    if len(context['latest_news_list']) == 0:
        return render(request, APP_LABEL + '/test_embedding.html')
    else:
        return render(request, APP_LABEL + '/test_embedding.html', context)


def research(request):
    return render(request, APP_LABEL + '/research.html')


def new(request):
    records = New.objects.exclude(text_ja="").order_by("-date")
    years = set(record.date.year for record in records)
    news = {year:[] for year in years}
    for record in records:
        news[record.date.year].append({
                "id": record.id, "date": str(record.date), "text_ja": record.text_ja, "image": record.image
            })
    news = sorted(news.items(), key=lambda x: -x[0])
    return render(request, APP_LABEL + '/new.html', context={"news":news})


def member(request):
    return render(request, APP_LABEL + '/member.html')