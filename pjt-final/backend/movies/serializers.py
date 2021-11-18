from rest_framework import serializers
from .models import Movie, Genre, Actor, Review


class GenreSerializer(serializers.ModelSerializer):
    class Movies(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title',)
    movies = Movies(many=True, read_only=True)

    id = serializers.IntegerField()
    class Meta:
        model = Genre
        fields =('id', 'name', 'movies')
        read_only_fields = ('movies',)


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'poster_path',)


# class MovieSerializer(serializers.ModelSerializer):
#     class Actors(serializers.ModelSerializer):
#         class Meta:
#             model = Actor
#             fields = ('id', 'name')
#     class Genres(serializers.ModelSerializer):
#         class Meta:
#             model = Genre
#             fields = ('id', 'name')
    
#     genre_ids = serializers.ListField(write_only=True)

#     def create(self, validated_data):
#         genre_ids = validated_data.pop('genre_ids')
#         movie = Movie.objects.create(**validated_data)
#         for genre_pk in genre_ids:
#             movie.genres.add(genre_pk)
#         return movie

#     def update(self, movie, validated_data):
#         #actor = instance
#         genre_ids = validated_data.pop('genre_ids')
#         for attr, value in validated_data.items():
#             setattr(movie, attr, value)
#         movie.save()

#         movie.genres.clear()
#         for genre_pk in genre_ids:
#             movie.genres.add(genre_pk)
#         return movie

#     class Meta:
#         model = Movie
#         fields = '__all__'


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        pass


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        pass




class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        pass


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        pass