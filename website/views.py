from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Category, News
from .forms import ContactForm


def home(request):
    categories = Category.objects.all()

    latest = News.objects.filter(status='PB').order_by('-publish_time').first()
    latest6 = News.objects.filter(status='PB').order_by('-publish_time').iterator(chunk_size=6)
    context = {
        'latest': latest,
        'latest6': latest6,
        'latest_news': {
            category.slug: {
                'first': News.objects.filter(status='PB', category__slug=category.slug).first(),
                 'all': News.objects.filter(status='PB', category=category).order_by('-publish_time')[1:5],
                }
            for category in categories
        },
    }

    return render(request, 'index.html', context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse('<h1>Succes</h1>')

    return render(request, 'contact.html')

def get_news_list(request):
    news_list = News.objects.filter(status='PB')
    context = {'news': news_list}
    return render(request, 'test/news_list.html', context)

def get_new_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'test/new_detail.html', {
        'news': news
    })

def get_news_by_category(request,category):
    category_obj = get_object_or_404(Category, slug=category)
    news = News.objects.filter(status='PB', category=category_obj)
    context = {'news': news}
    return render(request, 'test/news_list.html', context)