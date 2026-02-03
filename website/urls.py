from django.urls import path
from website.views import get_news_list, get_new_detail, get_news_by_category, home

urlpatterns = [
    path('home/', home),
    path('all/', get_news_list),
    path('<slug:category>/', get_news_by_category),
    path('<slug:category>/<slug:slug>', get_new_detail)
]
