from django.urls import path
from MyApp import views

app_name = "userapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form')
]
