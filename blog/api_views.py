# API
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAdminUser

# Django
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.text import slugify

# Serializer
from .serializers import ArticleSerializer

# Model
from .models import Article



class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
