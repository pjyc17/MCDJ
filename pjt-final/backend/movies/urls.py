from django.urls import path
from . import views

urlpatterns = [
    path('TMDB/', views.TMDB),
    path('all/', views.all),
    path('<int:movie_id>/', views.movie),
    path('search/<keyword>/', views.search),
    path('annually_poster/', views.annually_poster),
    path('annual_movies/<int:year>/', views.annual_movies),
    path('chat/<int:movie_id>/', views.chat),
    path('delete/<int:chat_id>/', views.delete),
    path('genre/<int:genre_id>/', views.genre),
    path('actor/<int:actor_id>/', views.actor),
]