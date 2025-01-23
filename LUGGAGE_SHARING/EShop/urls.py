from django.contrib import admin
from django.urls import path
from EShop import views

urlpatterns = [
    path("",views.HomePage,name='EShop'),
    path("login",views.loginUser,name='login'),
    path("logout",views.logoutUser,name='logout')
     
]