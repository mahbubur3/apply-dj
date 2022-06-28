from django.shortcuts import render
from django.http import HttpResponse
from MyApp import forms
from MyApp.models import Actor, Movie


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
    data = {
        'title': "Movies",
        'actor_info': actor_info,
        'movie_list': movie_list,
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


def edit_actor(request, actor_id):
    actor_info = Actor.objects.get(pk=actor_id)
    form = forms.ActorForm(instance=actor_info)

    if request.method == 'POST':
        form = forms.ActorForm(request.POST, instance=actor_info)

        if form.is_valid():
            form.save(commit=True)
            return movie_list(request, actor_id)

    data = {'edit_form': form}
    return render(request, 'my_app/edit_actor.html', context=data)


def edit_movie(request, movie_id):
    movie_info = Movie.objects.get(pk=movie_id)
    form = forms.MovieForm(instance=movie_info)
    data = {}
    if request.method == 'POST':
        form = forms.MovieForm(request.POST, instance=movie_info)

        if form.is_valid():
            form.save(commit=True)
            data.update({'success_text': 'Updated'})

    data.update({'edit_form': form})
    data.update({'movie_id': movie_id})
    return render(request, 'my_app/edit_movie.html', context=data)


def delete_movie(request, movie_id):
    form = Movie.objects.get(pk=movie_id).delete()
    data = {'delete_success': 'Deleted!'}
    return render(request, 'my_app/delete.html', context=data)


def delete_actor(request, actor_id):
    actor = Actor.objects.get(pk=actor_id).delete(0)
    data = {'delete_success': 'Deleted!'}
    return render(request, 'my_app/delete.html', context=data)
