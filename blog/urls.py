from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('post/', views.add_post, name='blog-post-add'),
    path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'),
    path('profile/', views.view_profile, name='profile'),
    path('profile_edit/<int:id>/', views.profile_edit, name='profile_edit'),
]
