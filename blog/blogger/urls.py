# from django.contrib import admin
from django.urls import path
# from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView
from . import views
# django.contrib.auth.views.LoginView
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    
]