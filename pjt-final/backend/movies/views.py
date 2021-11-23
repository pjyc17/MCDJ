import requests
from datetime import datetime
from random import choice
from django.shortcuts import redirect, get_object_or_404, get_list_or_404
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.serializers import Serializer
from .serializers import GenreSerializer, MovieSerializer, ActorSerializer, MovieListSerializer, ChatSerializer, GenreListSerializer, LogSerializer, CartSerializer
from .models import Chat, Genre, Movie, Actor, Log, Cart
from django.db.models import Prefetch, Count, Q
from django.contrib.auth import get_user_model

TMDB_URL = 'https://api.themoviedb.org/3'
API_KEY = '843ed6063914aca6ab7f2fcf47870d67'

# Create your views here.
def TMDB(request):
    # if request.user == '떵유' or request.user == '주윤':
        get_genres = f"{TMDB_URL}/genre/movie/list?api_key={API_KEY}&language=ko-KR"
        genres_dict = requests.get(get_genres).json().get('genres')
        #장르들 조회 /장르 테이블 먼저 생성(ManyToMany필드 중에 한개는 먼저 만들고 참조관계 생성)
        for genre in genres_dict:
            if not Genre.objects.filter(pk=genre.get('id')).exists():
                serializer = GenreSerializer(data=genre)
                if serializer.is_valid():
                    serializer.save()
        page = 1
        while True:
            #인기영화 각 페이지마다 아래를 반복함
            get_popular = f"{TMDB_URL}/movie/popular?api_key={API_KEY}&language=ko-KR&page={page}"
            response = requests.get(get_popular).json()
            page = response.get('page')
            movies = response.get('results')
            #영화정보 한 페이지당 20개의 영화에 대해 반복함
            for movie in movies:
                movieId = movie.get('id')
                #영상여부확인
                get_videos = f"{TMDB_URL}/movie/{movieId}/videos?api_key={API_KEY}"
                videos = requests.get(get_videos).json().get('results')
                if videos:
                    for video in videos:
                        if video.get('site') == 'YouTube':
                            break
                    else:
                        continue
                    #영화테이블에 이미 존재하는 영화는 삭제
                    if Movie.objects.filter(pk=movieId).exists():
                        instance = Movie.objects.get(pk=movieId)
                        instance.delete()
                    #출연배우 3명 정보 요청
                    get_credit = f"{TMDB_URL}/movie/{movieId}/credits?api_key={API_KEY}&language=ko-KR"
                    casts = requests.get(get_credit).json().get('cast')[:3]
                    actor_ids = []
                    for cast in casts:
                        actorId = cast.get('id')
                        #배우테이블에 없는 배우 배우테이블에 추가
                        if not Actor.objects.filter(pk=actorId).exists():
                            serializer = ActorSerializer(data={'id': actorId, 'name': cast.get('name')})
                            if serializer.is_valid():
                                serializer.save()
                        actor_ids.append(actorId)
                    #배우id리스트 movie에 data에 추가
                    movie['actor_ids'] = actor_ids
                    movie['youtube_key'] = video.get('key')
                    serializer = MovieSerializer(data=movie)
                    if serializer.is_valid():
                        serializer.save()
            # 마지막 페이지면 반복문 종료
            if page >= response.get('total_pages'):
                break
            page += 1
        # 끝났으니 front 페이지로 이동
        return redirect('http://121.178.32.250:8080')


@api_view(['GET'])
@permission_classes([AllowAny])
def all(request):
    movies = Movie.objects.all().order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def genres(request):
    genres = Genre.objects.all()
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    genres = []
    genre_set = movie.genres.all()
    for genre in genre_set:
        genres.append({'name': genre.name, 'id': genre.id})
    actors = []
    actor_set = movie.actors.all()
    for actor in actor_set:
        actors.append({'name': actor.name, 'id': actor.id})
    chats = []
    chat_set = movie.chats.all() 
    for chat in chat_set:
        chats.append({'rating': chat.rating, 'created': chat.created, 'user': {'id': chat.user.id, 'username': chat.user.username}, 'content': chat.content, 'id': chat.id})
    chats.sort(key=lambda x: x['created'])

    return Response({**serializer.data, 'genres': genres, 'actors': actors, 'chats': chats})


@api_view(['GET'])
@permission_classes([AllowAny])
def search(request, keyword):
    movies = Movie.objects.filter(title__contains=keyword).order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def search_by_genre(request, genre_id, keyword):
    # movies = Movie.objects.prefetch_related(Prefetch('genres', queryset=Genre.objects.filter(pk=genre_id))).annotate(genres_cnt=Count('genres')).filter(~Q(genres_cnt=0), title__contains=keyword).order_by('-popularity')
    #########################################################################################################
    movies = Movie.objects.filter(genres__id=genre_id, title__contains=keyword).order_by('-popularity')######
    #########################################################################################################
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def annually_poster(request):
    current_year = datetime.today().year
    year = current_year
    poster_paths = []
    while True:
        posters = Movie.objects.filter(release_date__startswith=year).order_by('-popularity').values('poster_path')[:5]
        if not posters:
            if year == current_year:
                continue
            break
        item = choice(posters)
        item['year'] = year
        poster_paths.append(item)
        year -= 1
    poster_paths.sort(key=lambda x: x['year'])
    return Response({'chronology_poster': poster_paths})

@api_view(['GET'])
@permission_classes([AllowAny])
def annual_movies(request, year):
    movies = Movie.objects.filter(release_date__startswith=year).order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def genre(request, genre_id):
    movies = Movie.objects.prefetch_related('genres').filter(genres=genre_id).order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def actor(request, actor_id):
    movies = Movie.objects.prefetch_related('actors').filter(actors=actor_id).order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def chat(request, movie_id):
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer.save(user=request.user, movie=movie)
        return Response({**serializer.data, 'user': {'id': request.user.id, 'username': request.user.username}})

@api_view(['DELETE'])
def delete(request, chat_id):
    chat = get_object_or_404(Chat, pk=chat_id)
    if request.user == chat.user:
        chat.delete()
    return Response({'message': '삭제완료'})

@api_view(['POST'])
@permission_classes([AllowAny])
def log(request, movie_id):
    isCart = False ###cart때문에 넣음
    if request.user.pk == None:
        if not get_user_model().objects.filter(pk=0).exists():
            get_user_model().objects.create(pk=0, username="")
        user = get_object_or_404(get_user_model(), pk=0)
    else:
        user = request.user
        if user.carts.filter(movie__pk=movie_id).exists():
            isCart = True ###cart때문에 넣음
    serializer = LogSerializer(data=request.data)
    if serializer.is_valid():
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer.save(user=user, movie=movie)
        return Response({'isCart': isCart}) ###cart때문에 넣음

@api_view(['PUT'])
def cart(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_id)
    if user.carts.filter(movie__pk=movie_id).exists():
        cart = user.carts.get(movie=movie_id)
        cart.delete()
        return Response({'isCart': False})
    else:
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, movie=movie)
            return Response({'isCart': True})