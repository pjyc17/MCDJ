from django.db import models

# Create your models here.

class movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    released_date = models.DateField()
    poster_path = models.TextField
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    popularity = models.FloatField()
    genres = models.ManyToManyField(genre)

    def __str__(self):
        return f'title : {self.title}'

class actor(models.Model):
    name = models.varchar(100)
    movies = models.ManyToManyField(movie, related_name='actors')
    
    def __str__(self):
        return f'name: {self.name}'

class review(models.Model):
    movie_id = models.ForeignKey(movie, on_delete=models.CASCADE)
    title = models.varchar(100)
    content = models.TextField()
    rank = models.IntegerField()

    def __str__(self):
        return f'{self.movie_id}, {self.title}'
    
class genre(models.Model):
    name = models.varchar(50)

