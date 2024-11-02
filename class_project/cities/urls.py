from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('city/<int:pk>', views.city, name='city'),
    path('create_city/', views.create_city, name='create_city'),
    path('update_city/<int:pk>', views.update_city, name='update_city'),
    path('delete_city/<int:pk>', views.delete_city, name='delete_city'),
]
