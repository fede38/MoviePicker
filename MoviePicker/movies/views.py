from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Movie


def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("La pelicula consultada no existe")
    return render(request, 'movie/detail.html', {'movie': movie})
