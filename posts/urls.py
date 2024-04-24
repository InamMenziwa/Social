from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.feed, name="feed"),
    path('create', views.PostCreate, name="postcreate"),
    path('like/', views.like_post, name="like_post"),
 ] 