
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.Home, name="home"),
    path('add', views.AddProduct, name="add"),


]
