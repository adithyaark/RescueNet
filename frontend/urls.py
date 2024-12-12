from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default landing page
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('support/', views.support, name='support'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('add-disaster/', views.add_disaster, name='add-disaster'),
]
