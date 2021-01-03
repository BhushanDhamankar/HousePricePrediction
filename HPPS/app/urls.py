from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('', views.home, name="home"),
    path('predict/', views.predict, name="predict"),
    path('predict/result', views.result, name="result"),
]