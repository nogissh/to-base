from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
  path('', views.Root),
  path('home/', views.Home),
  path('profile/', views.Profile)
]
