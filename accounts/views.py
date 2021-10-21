from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy



class LoginUser(auth_views.LoginView):
    template_name = 'accounts/login.html'



class LogoutUser(auth_views.LogoutView):
    next_page = 'blog:all_articles'