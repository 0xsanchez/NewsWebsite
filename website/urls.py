from django.urls import path
from website.views import get_news_list, get_new_detail


urlpatterns = [
    path('news/', get_news_list),
    path('new/<slug:slug>/', get_new_detail),
]
