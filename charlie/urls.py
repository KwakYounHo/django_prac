from django.urls import path, include
from charlie import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<int:id>', views.read),
    path('delete', views.delete),
    path('update/<int:id>', views.update)
]