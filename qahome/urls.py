from django.contrib import admin
from django.urls import path
from qahome import views

#url for index view
urlpatterns = [
    path('', views.index, name = "index" ),
]
