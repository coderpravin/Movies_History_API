from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie
# Create your views here.

def movieView(request):
    movies = list(Movie.objects.all().values())
    return JsonResponse(movies, safe=False)
