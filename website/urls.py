from django.urls import path
from website.views import get_news_list, get_new_detail, get_news_by_category, home, contact

urlpatterns = [
    path('', home, name='home_page'),
    paht('contact',contact, name='contact_page'),
    path('all/', get_news_list, name='news_page'),
    path('<slug:category>/', get_news_by_category),
    path('<slug:category>/<slug:slug>', get_new_detail)
]
