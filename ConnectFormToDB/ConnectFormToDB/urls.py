from django.contrib import admin
from django.urls import path
from MyApp import views

app_name = 'my_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('form/', views.form, name='form')
]
