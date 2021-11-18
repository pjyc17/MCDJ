from django.urls import path
from . import views

urlpatterns = [
    path('TMDB/', views.TMDB),
    path('<int:movie_id>/', views.movie),
    path('search/<keyword>/', views.search),
    path('annually_poster/', views.annually_poster),
    path('annual_movies/<int:year>/', views.annual_movies),
    path('chat/<int:movie_id>/', views.chat),
    path('delete/<int:chat_id>/', views.delete),
]