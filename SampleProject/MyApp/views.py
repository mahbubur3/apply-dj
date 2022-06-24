from django.shortcuts import render
from django.http import HttpResponse
from MyApp import forms
from MyApp.models import Actor, Movie
from django.db.models import Avg


def home(request):
    actors = Actor.objects.order_by('name')
    data = {
        'title': "HOME",
        'actors': actors
    }
    return render(request, 'my_app/home.html', context=data)


def movie_list(request, actor_id):
    actor_info = Actor.objects.get(pk=actor_id)
    movie_list = Movie.objects.filter(
        actor=actor_id).order_by('movie_name', 'release_date')
    actor_rating = Movie.objects.filter(
        actor=actor_id).aggregate(Avg('rating_star)'))
    data = {
        'title': "Movies",
        'actor_info': actor_info,
        'movie_list': movie_list,
        'actor_rating': actor_rating,
    }
    return render(request, 'my_app/movie_list.html', context=data)


def add_actor_form(request):
    form = forms.ActorForm()

    if request.method == 'POST':
        form = forms.ActorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)

    data = {
        'title': "Add Actor",
        'actor_form': form
    }
    return render(request, 'my_app/add_actor.html', context=data)


def add_movie_form(request):
    form = forms.MovieForm()

    if request.method == 'POST':
        form = forms.MovieForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)

    data = {
        'title': "Add Movie",
        'movie_form': form,
    }
    return render(request, 'my_app/add_movie.html', context=data)
