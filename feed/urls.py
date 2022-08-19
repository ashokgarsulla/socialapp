from django.contrib import admin
from django.urls import path

from .views import feed_view,post_list_view

app_name = 'accounts'

urlpatterns = [
    path('', feed_view, name='feed'),
    path('postlist',post_list_view, name='postlist'),
    
    
]