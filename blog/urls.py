from django.urls import path
from . import views
from .views import PostList

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('add/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit/<slug:slug>/', views.edit_blog_post, name='edit_blog_post'),
    path(
        'delete/<int:post_id>/',
        views.delete_blog_post, name='delete_blog_post'),
]
