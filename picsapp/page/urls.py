from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('single/<str:pk>/', views.viewPic, name='single'),
    path('add/', views.addPic, name='add'),
]