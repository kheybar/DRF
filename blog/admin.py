from django.contrib import admin
from .models import Article, Category



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'writer', 'slug', 'published', 'status']
    list_filter = ['published', 'status']
    search_fields = ('title', 'body')
    list_editable = ('status',)



admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)