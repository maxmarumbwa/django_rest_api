"""from django.shortcuts import render
from app.models import Movie
from django.http import JsonResponse


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    data = {"movies": list(movies.values())}
    return JsonResponse(data)


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    data = {
        "id": movie.id,
        "name": movie.name,
        "description": movie.description,
        "active": movie.active,
    }
    return JsonResponse(data)
"""
