from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Category, News

def get_news_list(request):
    news_list = News.objects.filter(status='published')
    context = {'news': news_list}
    return render(request,'test/news_list.html',context)

def get_new_detail(request,slug):
    new = get_object_or_404(News, slug=slug)
    context = {'new': new}
    return render(request,'test/new_detail.html',context)