from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
  path('principal', views.obterPrincipal, name='menu-principal'),
  path('init', views.start, name='menu-init'),
  path('chat', views.postData, name='menu-chat')

  ##path('chat', views.start, name='menu-chat'),
]