from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .api_urls import router



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]

# API
urlpatterns += [
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
