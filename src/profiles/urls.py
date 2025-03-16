from django.contrib import admin
from django.urls import path,include
from .views import profile_detail_view, profile_list_view

urlpatterns = [
    path("<username>/",profile_detail_view),  
    path("",profile_list_view)
]
