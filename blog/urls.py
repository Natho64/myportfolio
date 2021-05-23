from django.urls import path
from . import views
from django.contrib import admin
from personal_portfolio import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('<int:blog_id>', views.detail, name = 'detail'),
]

