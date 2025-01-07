from django.contrib import admin
from django.urls import path
from EShop import views

urlpatterns = [
    path("",views.index,name='EShop')
     
]