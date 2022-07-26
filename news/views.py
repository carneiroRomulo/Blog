from django.shortcuts import get_object_or_404, render

from .models import News


def home(request):
    news_list = News.objects.filter(status='p')
    return render(request, 'news/pages/home.html', context={
        'news_list': news_list,
    })


def news(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news/pages/news.html', context={
        'news': news,
        'is_detail_page': True,
    })
