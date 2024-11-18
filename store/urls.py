from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
   path('about/',views.about,name='about'),
   path('login_user/',views.login_user,name='login_user'),
   path('logout_user/',views.logout_user,name='logout_user'),
   path('register_user/',views.register_user,name='register_user'),
   path('getProduct/<int:pk>',views.getProduct,name='getProduct'),
   path('getCategoryProduct/<int:pk>',views.getCategoryProduct,name='getCategoryProduct')
]
