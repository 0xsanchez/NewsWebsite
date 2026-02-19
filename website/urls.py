from django.urls import path
from website.views import get_news_list, get_new_detail, get_news_by_category, home, contact, NewsCreateView, NewsDeleteView, NewsUpdateView

urlpatterns = [
    path('', home, name='home_page'),
    path('contact/',contact, name='contact_page'),
    path('all/', get_news_list, name='news_page'),
    path('category/<slug:category>/', get_news_by_category, name='category_news'),
    path('news/<slug:slug>', get_new_detail, name='news_detail'),
    path('news/<slug:slug>/delete', NewsDeleteView.as_view(), name='news_delete'),
    path('news/<slug:slug>/update', NewsUpdateView.as_view(), name='news_update'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
]
