from django.urls import path
from . import views

urlpatterns = [
    path('TMDB/', views.TMDB),
    path('all/', views.all),
    path('genres/all/', views.genres),
    path('<int:movie_id>/', views.movie),
    path('annually_poster/', views.annually_poster),
    path('annual_movies/<int:year>/', views.annual_movies),
    path('genre/<int:genre_id>/', views.genre),
    path('actor/<int:actor_id>/', views.actor),
    ###검색###
    path('search/<keyword>/', views.search),
    path('<int:genre_id>/search/<keyword>/', views.search_by_genre),
    ###관계###
    path('<int:movie_id>/chat/', views.chat),
    path('delete/<int:chat_id>/', views.delete),
    path('log/<movie_id>/', views.log),
    path('cart/<movie_id>/', views.cart),
    ###추천###
    path('recommend/all/', views.recom_all),
    path('recommend/every_genre/', views.recom_every_genres),
    path('recommend/<int:year>/', views.recom_by_year),

    ###프로필###
    path('recommend/genres/<birthday>/<int:user_id>/', views.recom_genres), # ex) 1225
    path('user_cart/<int:user_id>/', views.user_cart),
]