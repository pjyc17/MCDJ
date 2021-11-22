from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    popularity = models.FloatField()
    youtube_key = models.CharField(max_length=100)

    def __str__(self):
        return f'title : {self.title}'

class Genre(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='genres')

class Actor(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='actors')
    
    def __str__(self):
        return f'name: {self.name}'

class Chat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='chats')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chats')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.movie_id}, {self.content}'
    

