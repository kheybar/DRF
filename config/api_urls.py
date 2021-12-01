from rest_framework import routers
from blog.api_views import ArticleViewset



router = routers.SimpleRouter()
router.register('article', ArticleViewset, basename='article')