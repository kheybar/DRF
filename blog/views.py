from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from .models import Article, TestSerializer

# API
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Serializer
from .serializers import ArticleSerializer, TestsSerializer



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




# API

@api_view(['GET', 'POST']) # Accept Methods
def response_api(request):
    """
        this function for test and use Response Method.
    """
    if request.method == 'POST':
        name = request.data['name'] # deserialize
        return Response({'name': f'your name is {name}'}) # serialize

    elif request.method == 'GET':
        return Response({'name': 'Boss'}) # serialize


@api_view()
def test_serializer(request):
    db_info = TestSerializer.objects.all()
    serialize_info = TestsSerializer(db_info, many=True)
    return Response(serialize_info.data)



class AllArticleApi(APIView):
    
    def get(self, request, format=None):
        articles = Article.objects.all()
        serialize_articles = ArticleSerializer(articles, many=True)
        return Response(serialize_articles.data)



class ArticleApi(APIView):

    def get(self, request, format=None, **kwargs):
        article = get_object_or_404(Article, id=self.kwargs['article_id'])
        serialize_article = ArticleSerializer(article)
        return Response(serialize_article.data)