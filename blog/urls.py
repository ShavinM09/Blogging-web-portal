
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('user/<str:username>', SUserPostListView.as_view(), name='suser-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name="post-detail"),
    path('post/new/', PostcreateView.as_view(),name="post-create"),
    path('post/<int:pk>/update/', PostupdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/', PostdeleteView.as_view(),name="post-delete"),
    path('about/', views.about,name="blog-about")

]

