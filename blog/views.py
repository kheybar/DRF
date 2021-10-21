from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.text import slugify
from .models import Article



class AllArticle(generic.ListView):
    queryset = Article.publish_filter.all()
    template_name = 'blog/all_articles.html'
    context_object_name = 'all_articles'
    ordering = ('-created')



class ArticleDetail(generic.DetailView):
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
    def get_queryset(self, **kwargs):
        return Article.objects.filter(id=self.kwargs['pk'], slug__iexact=self.kwargs['slug'])



class ArticleCreate(generic.CreateView):
    model = Article
    fields = ('title', 'slug', 'body')
    success_url = reverse_lazy('blog:all_articles')
    template_name = 'blog/article_create.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.writer = self.request.user
        article.status = 'publish'
        article.save()
        messages.success(self.request, 'your article create.', extra_tags='success')
        return super().form_valid(form)



class ArticleDelete(generic.DeleteView):
    model = Article
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('blog:all_articles')



class ArticleUpdate(generic.UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'blog/article_update.html'
    success_url = reverse_lazy('blog:all_articles')
    
    def form_valid(self, form):
        article = form.save()
        messages.success(self.request, 'مقاله شما با موفقیت بروزرسانی شد', extra_tags='success')
        return super().form_valid(form)