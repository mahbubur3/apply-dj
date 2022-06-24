from django.urls import path
from MyApp import views

app_name = "your_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('addmovie/', views.add_movie_form, name="add_movie_form"),
    path('addactor/', views.add_actor_form, name="add_actor_form"),
    path('movielist/<int:actor_id>/', views.movie_list, name="movie_list"),
]
