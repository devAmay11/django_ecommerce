from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
   path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
   path('view_cart/',views.view_cart,name='view_cart'),
]
