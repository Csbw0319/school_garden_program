from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('info/', views.info, name='school-gardens'),
   path('accounts/profile', views.ProfileView.as_view(), name="profile"), 
   path('learnmore/', views.learnmore, name='learnmore'),
   path('create/', views.create, name='create'),
   path('update_volunteer/<volunteer_id>', views.update_volunteer, name='update-volunteer'),
   path('delete/', views.delete, name='delete'),
   path('thankyou/', views.thankyou, name='thankyou'),
   path('accounts/volunteer/', views.volunteer, name='volunteer'),
   
   #Auth
   path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
   path('accounts/logout', auth_views.LogoutView.as_view(), name="logout")
]