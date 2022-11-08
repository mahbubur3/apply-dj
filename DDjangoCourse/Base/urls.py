from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('works/', views.works, name='works'),
    path('work/<str:pk>/', views.work, name='work'), #pk er jaygay onno nam o deya jay
]
