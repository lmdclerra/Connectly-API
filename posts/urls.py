from django.urls import path, include 
from . import views 
from .views import UserListCreate, PostListCreate, CommentListCreate
from django.contrib import admin


urlpatterns = [
    # path('users/', views.get_users, name='get_users'),                          # http://127.0.0.1:8000/posts/users/
    path('users/create/', views.create_user, name='create_user'),               # http://127.0.0.1:8000/posts/users/create/
    path('users/read/<int:user_id>/', views.get_user, name='get_user'),         # http://127.0.0.1:8000/posts/users/read/1/
    path('users/update/<int:user_id>/', views.update_user, name='update_user'), # http://127.0.0.1:8000/posts/users/update/1/
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'), # http://127.0.0.1:8000/posts/users/delete/1/
    # path('posts/', views.get_posts, name='get_posts'),                          # http://127.0.0.1:8000/posts/posts/
    path('posts/create/', views.create_post, name='create_post'),               # http://127.0.0.1:8000/posts/posts/create/
  
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'), 
]   