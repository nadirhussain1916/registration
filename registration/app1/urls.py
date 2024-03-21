from django.contrib import admin
from django.urls import path
from app1 import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('', views.SignupPage, name='signup'),
    path('logout/', views.LogoutPage, name='logut'),
    path('create/', views.create_post, name='create_post'),
    path('posts/', views.post_list, name='post_list'),
]
