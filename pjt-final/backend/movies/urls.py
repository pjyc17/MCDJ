from django.urls import path
from . import views

urlpatterns = [
    path('TMDB/', views.TMDB),
    path('<keyword>/', views.search),
]