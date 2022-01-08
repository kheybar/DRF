from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'writer', 'title', 'slug', 'body')
        extra_tags = {
            'id': {'read_only': True}
        }
    
    def validate_title(self, value):
        if value == 'none':
            raise serializers.ValidationError('title can not be none')
        return value