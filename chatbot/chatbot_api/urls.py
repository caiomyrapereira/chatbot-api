from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
  path('init', views.start, name='menu-init'),
  path('chat', views.postData, name='menu-chat'),
]