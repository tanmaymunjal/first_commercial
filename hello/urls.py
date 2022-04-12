
from django.contrib import admin
from django.urls import path
from tanmay import views
urlpatterns = [
    path('',views.index),
    path('menu/',views.menu),
    path('contact/',views.contact),
    
]
