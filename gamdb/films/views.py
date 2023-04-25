from django.shortcuts import render
from .models import Movie, Director, Actor

def directors(request):
    context = {
        'title': "Herci",
        'directors': Director.objects.all()
    }
    return render(request, 'directors.html', context)


def homepage(request): #defines what is seen on the first page after executing runserver, has to be pathed in urls.py
    context = {
        "movies": Movie.objects.all()
    }
    return render(request, 'main.html', context)

def director(request, id):
    context = {
        "director": Director.objects.get(id=id)
    }
    return render(request, 'director.html', context)

def movies(request):
    context = {
        "movies": Movie.objects.all()
    }
    return render(request, 'movies.html', context)

def movie(request, id):
    context = {
        "movie": Movie.objects.get(id=id)
    }
    return render(request, 'movie.html', context)

def actors(request):
    context = {
        "actors": Actor.objects.all()
    }
    return render(request, 'actors.html', context)

def actor(request, id):
    context = {
        "actor": Actor.objects.get(id=id)
    }
    return render(request, 'actor.html', context)
