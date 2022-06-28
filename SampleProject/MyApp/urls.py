from django.urls import path
from MyApp import views

app_name = "your_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('addmovie/', views.add_movie_form, name="add_movie_form"),
    path('addactor/', views.add_actor_form, name="add_actor_form"),
    path('movielist/<int:actor_id>/', views.movie_list, name="movie_list"),
    path('editactor/<int:actor_id>/', views.edit_actor, name="edit_actor"),
    path('edit_movie/<int:movie_id>/', views.edit_movie, name="edit_movie"),
    path('deletemovie/<int:movie_id>/', views.delete_movie, name="delete_movie"),
    path('deleteactor/<int:actor_id>/', views.delete_actor, name="delete_actor"),
]
