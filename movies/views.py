""" http response """
from django.http import HttpResponse
from .models import Movie
from django.shortcuts import render, get_object_or_404

# Create your views here.


def index(request):
    """ index """
    movies = Movie.objects.all()
    return render(request, "movies/index.html", {"movies": movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, "movies/detail.html", {"movie": movie})
