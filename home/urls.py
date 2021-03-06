from django.contrib import admin
from django.urls import path,include
from home import views
from .views import *

urlpatterns = [
    
    path('', views.index, name="index"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('add_blog/',views.add_blog,name="add_blog"),
    path('register_page/', views.register_page, name="register_page"),
   
    path('blog_detail/<int:m_id>', views.blog_detail,name="blog_detail"),
]