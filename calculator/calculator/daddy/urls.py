from django.contrib import admin
from django.urls import path,include
from daddy import views

urlpatterns = [
    path("",views.index,name="daddy"),
    
]
