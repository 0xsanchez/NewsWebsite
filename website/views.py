from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Category, News
from .forms import ContactForm


def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
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

def get_new_detail(request, category, slug):
    category_obj = get_object_or_404(Category, slug=category)
    news_item = get_object_or_404(News, slug=slug, category=category_obj)
    return render(request, 'test/new_detail.html', {
        'new': news_item
    })

def get_news_by_category(request,category):
    category_obj = get_object_or_404(Category, slug=category)
    news = News.objects.filter(status='PB', category=category_obj)
    context = {'news': news}
    return render(request, 'test/news_list.html', context)