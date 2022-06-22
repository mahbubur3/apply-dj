from django.urls import path
from YourApp import views

app_name = "userapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
]
