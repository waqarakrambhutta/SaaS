from django.contrib import admin
from django.urls import path,include
from .views import profile_view

urlpatterns = [
    path("<username>/",profile_view),  
]
