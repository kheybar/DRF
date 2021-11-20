from rest_framework import serializers



class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    slug = serializers.SlugField()
    body = serializers.CharField()



class TestsSerializer(serializers.Serializer):
    title = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()