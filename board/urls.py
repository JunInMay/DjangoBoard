from django.contrib import admin
from django.urls import path

from board import views

urlpatterns = [
    path('', views.index),
]