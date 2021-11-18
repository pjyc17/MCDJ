from django.shortcuts import render, redirect
import requests
from .serializers import GenreSerializer
from .models import Genre
TMDB_URL = 'https://api.themoviedb.org/3'
API_KEY = '843ed6063914aca6ab7f2fcf47870d67'

# Create your views here.
def TMDB(requst):
    get_genres = f"{TMDB_URL}/genre/movie/list?api_key={API_KEY}"
    genres_dict = requests.get(get_genres).json().get('genres')

    for genre in genres_dict:
        if not Genre.objects.filter(pk=genre.get('id')).exists():
            serializer = GenreSerializer(data=genre)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    page = 1
    while True:
        get_popular = f"{TMDB_URL}/movie/popular?api_key={API_KEY}&page={page}"
        response = requests.get(get_popular).json()
        page = response.get('page')
        movies = response.get('results')
        for movie in movies:
            print(movie)
        if page >= response.get('total_pages'):
            break
        page += 1

    return redirect('http://google.com')




def search(request, keyword):
    pass