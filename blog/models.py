from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish')


class Article(models.Model):
    STATUS = (
        # first: DB, second: in admin
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    )

    title = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, default=None, null=True)
    slug = models.SlugField(max_length=150, unique=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='متن مقاله')
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    
    # customize Manager
    objects = models.Manager() # active default manager
    publish_filter = PublishedArticleManager() # customize manager


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=(self.id, self.slug))

    def writer_name(self):
        return f'{self.writer.first_name} {self.writer.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name