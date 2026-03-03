from django.urls import path
from .views import user_login, user_logout, profile_view, register_view, edit_profile

urlpatterns = [
    path('login/', user_login, name='login_page'),
    path('logout/', user_logout, name='logout_page'),
    path('profile/', profile_view, name='profile_page'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('register/', register_view, name='reg_page')
]