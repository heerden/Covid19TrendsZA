from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forecast/', views.forecast, name='forecast'),
    path('export/', views.export, name='export'),
    path('matplot/', views.matplot, name='matplot'),
    path('snapshot/', views.snapshot, name='snapshot')
]
