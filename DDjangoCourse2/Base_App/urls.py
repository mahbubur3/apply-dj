from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('works/', views.works, name='works'),
    path('work/', views.work, name='work'),
]