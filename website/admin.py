from django.contrib import admin

# Register your models here.
from .models import Category, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','publish_time','status']
    list_filter = ['status']
    
    search_fields = ['title','slug']
    prepopulated_fields = {'slug': ('title',)}