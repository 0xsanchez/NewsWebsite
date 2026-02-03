from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class News(models.Model):

    class StatusChoices(models.TextChoices):
        Draft = 'DF','draft'
        Published = 'PB','published'
    
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/')
    publish_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,choices=StatusChoices.choices,default=StatusChoices.Draft)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

        ordering = ['-publish_time']