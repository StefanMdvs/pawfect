from django.urls import path
# from . import views
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
