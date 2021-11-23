from django.urls import path
from . import views

urlpatterns = [
    path('TMDB/', views.TMDB),
    path('all/', views.all),
    path('genres/all/', views.genres),
    path('<int:movie_id>/', views.movie),
    path('search/<keyword>/', views.search),
    path('<int:genre_id>/search/<keyword>/', views.search_by_genre),
    path('annually_poster/', views.annually_poster),
    path('annual_movies/<int:year>/', views.annual_movies),
    path('<int:movie_id>/chat/', views.chat),
    path('delete/<int:chat_id>/', views.delete),
    path('genre/<int:genre_id>/', views.genre),
    path('actor/<int:actor_id>/', views.actor),
    path('log/<movie_id>/', views.log),
    path('cart/<movie_id>/', views.cart),
]