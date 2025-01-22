from django.urls import path 
from . import views


urlpatterns = [
    path('users/', views.get_users, name='get_users'),                          # http://127.0.0.1:8000/posts/users/
    path('users/create/', views.create_user, name='create_user'),               # http://127.0.0.1:8000/posts/users/create/
    path('users/read/<int:user_id>/', views.get_user, name='get_user'),         # http://127.0.0.1:8000/posts/users/read/1/
    path('users/update/<int:user_id>/', views.update_user, name='update_user'), # http://127.0.0.1:8000/posts/users/update/1/
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'), # http://127.0.0.1:8000/posts/users/delete/1/
    path('posts/', views.get_posts, name='get_posts'),                          # http://127.0.0.1:8000/posts/posts/
    path('posts/create/', views.create_post, name='create_post'),               # http://127.0.0.1:8000/posts/posts/create/
]