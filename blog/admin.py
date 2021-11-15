from django.contrib import admin
from .models import Article, TestSerializer

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'writer', 'slug', 'published', 'status']
    list_filter = ['published', 'status']
    search_fields = ('title', 'body')
    list_editable = ('status',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(TestSerializer)