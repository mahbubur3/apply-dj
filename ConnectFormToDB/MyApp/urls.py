from django.urls import path
from MyApp import views


app_name = "demo"


urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
]
