from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView


from .models import Category, News
from .forms import ContactForm


def home(request):
    categories = Category.objects.all()

    latest = News.objects.filter(status='PB').order_by('-publish_time').first()
    latest6 = News.objects.filter(status='PB').order_by('-publish_time').iterator(chunk_size=6)
    context = {
        'user': request.user,
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
    return render(request, 'news_detail.html', {
        'news': news
    })

def get_news_by_category(request,category):
    category_obj = get_object_or_404(Category, slug=category)
    news = News.objects.filter(status='PB', category=category_obj)
    context = {'news': news, 'category_name': category_obj.name}
    return render(request, 'category.html', context)

class NewsCreateView(CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('category', 'title', 'image', 'body', 'status')
    success_url = reverse_lazy('home_page')

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    context_object_name = 'news'
    success_url = reverse_lazy('home_page')

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'crud/news_update.html'
    fields = ('category', 'title', 'image', 'body', 'status')
    context_object_name = 'news'
    success_url = reverse_lazy('home_page')