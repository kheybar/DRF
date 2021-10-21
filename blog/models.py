from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User



class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish')



class Article(models.Model):
    STATUS = (
        ('draft', 'درحال توسعه'),
        ('publish', 'منتشر شده'),
    )

    title = models.CharField(max_length=150, unique=True, verbose_name='عنوان')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='آدرس مقاله')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    body = models.TextField(verbose_name='متن مقاله')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    published = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان آپدیت')
    status = models.CharField(max_length=20, choices=STATUS, default='draft', verbose_name='وضعیت')
    
    # customize Manager
    objects = models.Manager() # active default manager
    publish_filter = PublishedArticleManager() # customize manager


    class Meta:
        verbose_name = 'مقاله'
        # verbose_name_plurall = 'مقاله ها'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=(self.id, self.slug))







