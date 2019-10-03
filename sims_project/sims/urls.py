from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.IndexListView.as_view(), name='home'), 
]