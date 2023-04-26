#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #esta siendo controlada por una vista
    path('test/', views.test, name="test"), 
    path('create/', views.create, name="create"),
    path('delete/', views.delete, name="delete"),
    #path('update/<int:pk>/', views.update, name="update"),
    #path('delete/<int:pk>/', views.delete, name="delete"),
    #path('list/', views.list, name="list"),
    
]
