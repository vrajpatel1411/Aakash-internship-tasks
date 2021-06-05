from django.urls import path
from myapp import views

urlpatterns = [
   path('',views.vraj,name="vraj"),
   path('about',views.about,name="about"),
   path('home',views.home,name="home"),
   path('contact',views.contact,name="contact"),
]
