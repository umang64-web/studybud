from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('room/<int:roomno>', views.room, name = "room"),
    path('main/', views.main, name = "main"),
    path('index/', views.index, name = "index"),
    path('info/', views.methodinfo, name = "methodinfo"),
    path('get/', views.getdata, name = "getdata"),
    
]
