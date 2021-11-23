from rest_framework import serializers
from .models import Movie, Genre, Actor, Chat, Cart, Log


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)

class GenreSerializer(serializers.ModelSerializer):
    class Movies(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title',)
    movies = Movies(many=True, read_only=True)

    id = serializers.IntegerField()
    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies')
        read_only_fields = ('movies',)


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path',)


class MovieSerializer(serializers.ModelSerializer):
    # class Actors(serializers.ModelSerializer):
    #     class Meta:
    #         model = Actor
    #         fields = ('id', 'name')
    # class Genres(serializers.ModelSerializer):
    #     class Meta:
    #         model = Genre
    #         fields = ('id', 'name')
    
    actor_ids = serializers.ListField(write_only=True)
    genre_ids = serializers.ListField(write_only=True)
    id = serializers.IntegerField()

    def create(self, validated_data):
        genre_ids = validated_data.pop('genre_ids')
        actor_ids = validated_data.pop('actor_ids')
        movie = Movie.objects.create(**validated_data)
        for genre_pk in genre_ids:
            movie.genres.add(genre_pk)
        for actor_pk in actor_ids:
            movie.actors.add(actor_pk)
        return movie

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'release_date', 'poster_path', 'vote_count', 'vote_count', 'vote_average', 'popularity', 'youtube_key', 'genre_ids', 'actor_ids')

    # def update(self, movie, validated_data):
    #     #actor = instance
    #     genre_ids = validated_data.pop('genre_ids')
    #     for attr, value in validated_data.items():
    #         setattr(movie, attr, value)
    #     movie.save()

    #     movie.genres.clear()
    #     for genre_pk in genre_ids:
    #         movie.genres.add(genre_pk)
    #     return movie

class ActorSerializer(serializers.ModelSerializer):
    class Movies(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title',)
    movies = Movies(many=True, read_only=True)

    id = serializers.IntegerField()
    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies')
        read_only_fields = ('movies',)


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'content', 'rating', 'created',)


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ('id',)

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ('id',)