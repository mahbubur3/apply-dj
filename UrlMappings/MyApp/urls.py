# from django.urls import re_path
from django.urls import path
from MyApp import views

urlpatterns = [
    path('', views.output, name='output')
]
