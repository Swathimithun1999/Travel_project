from . import views

from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),

   # path('about/',views.about,name='about'),
   #path('add/',views.addition,name='addition'),
   #path('sub/',views.substraction,name='addition'),
   # path('thanks/', views.thanks, name='thanks'),
]