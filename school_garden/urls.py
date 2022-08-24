from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
   path('', views.index, name='index'),
   path('profile/', views.profile, name='profile'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('login/', views.login, name='login'),
   path('info/', views.info, name='school gardens'),


]