## 11.16
- 기본 설정들 allauth, cors, jwt 적용   
## 11.17 팀 로고, 방향, 모델
- [MCDJ 로고](https://www.wix.com/logo/maker/esh/zoe-templates?companyName=mcdj&industry=%7B%22industry%22%3A%22dd%22%2C%22isCustom%22%3Atrue%7D&tags=dynamic%2Cfun%2Ccreative&logoPurpose=website&tid=3ba5f5c3-f513-482c-80fe-7f9a2bb19d96&referralAdditionalInfo=arenaSplitPage) & [favicon 제작](https://realfavicongenerator.net/)   
- 강아지 움짤 제작   
- 배경 디스코드 채팅색 적용   
- 로그인, 로그아웃, 회원가입 적용(bootstrap모달 적용했지만, 직접 만들계획), google로그인 새창띄움했지만, 오류가 있음   
- django accounts/models.py 초안 작성   

## 11.18 완벽한 백엔드를 위하여
- serializers   
역시 데이터 모델링이 가장 어렵다,, 어떤 정보들을 받아서 저장할지 모델은 이미 만들어졌지만, 유효성검사를 위해 다시 점검했다.   
```py
class MovieSerializer(serializers.ModelSerializer):

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
        fields = ('id', 'title', 'overview', 'release_date', 'poster_path', 'vote_count', 'vote_count', 'vote_average', 'popularity', 'genre_ids', 'actor_ids')
```
(다른 serializer는 평범하게 생겼음)   
movie를 저장할때, N:M관계여서 영화하나에 배우랑 장르가 여러개가 들어간다.   
따라서, 영화배우랑 장르는 id값을 리스트로 받기 위해, 리스트필드로 설정하고, 생성시, for문을 사용하여 movie_genre, movie_actor 테이블에 추가해준다.   


- view   

/////////////////////////////////////////////////////////////////////   

진짜 어려웠던, DB에 영화들 저장, 다 저장하고 나니, db가 11메가가 넘었다.   

```py
def XXXX(request):
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
                if requests.get(get_videos).json().get('results'):
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
                    serializer = MovieSerializer(data=movie)
                    if serializer.is_valid():
                        serializer.save()
            # 마지막 페이지면 반복문 종료
            if page >= response.get('total_pages'):
                break
            page += 1
        # 끝났으니 front 페이지로 이동
        return redirect('http://121.178.32.250:8080')
```

![image-20211119043542188](README_D.assets/image-20211119043542188-16372641441245.png)



/////////////////////////////////////////////////////////////////////   

좀 어려웠던 영화 세부정보   

기본적인 영화정보에, 장르이름들, 배우 이름들(3개), 챗 내용들을 추가로 넣어서 응답해준다.   

```py
@api_view(['GET'])
@permission_classes([AllowAny])
def movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    genres = []
    genre_set = movie.genres.all()
    for genre in genre_set:
        genres.append(genre.name)
    actors = []
    actor_set = movie.actors.all()
    for actor in actor_set:
        actors.append(actor.name)
    chats = []
    chat_set = movie.chats.all() 
    for chat in chat_set:
        chats.append({'created': chat.created, 'user': chat.user.username, 'content': chat.content})
    chats.sort(key=lambda x: x['created'])

    return Response({'movies': serializer.data, 'genres': genres, 'actors': actors, 'chats': chats})


@api_view(['GET'])
@permission_classes([AllowAny])
def search(request, keyword):
    movies = Movie.objects.filter(title__contains=keyword).order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
```

![image-20211119043252169](README_D.assets/image-20211119043252169-16372639734674.png)



/////////////////////////////////////////////////////////////////////   
각 해마다 인기순으로 정렬한 영화정보에서 poster_path 정보만 앞에서 5개 가져온 것에서 랜덤으로 1개씩 뽑아 리스트에 담아, 응답을 보내줌   
각종 ORM을 사용하여, poster정보를 골라 읽었다.
db는 저장하는 것보다 역시 읽어오는게 재밌다.   

```python
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
```
![image-20211119012507995](README_D.assets/image-20211119012507995-16372527139241.png)

![image-20211119042839930](README_D.assets/image-20211119042839930-16372637235732.png)

/////////////////////////////////////////////////////////////////////   
Chat 생성, 삭제 요청   
chat을 생성할 때, user뿐만 아니라, movie 테이블과도 엮여있었다.   
user만 엮여있는 경우는 수업시간에 해봤지만, 이번 케이스는 처음이였다.   
serializer에서 movie를 추가해줄려했지만, 아래 방법이 가장 간단한거 같다.   
```py
@api_view(['POST'])
def chat(request, movie_id):
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data)

@api_view(['delete'])
def delete(request, chat_id):
    chat = get_object_or_404(Chat, pk=chat_id)
    if request.user == chat.user:
        chat.delete()
    return Response({'message': '삭제완료'})
```

![image-20211119043005293](README_D.assets/image-20211119043005293-16372638066723.png)



- 영화 DB 저장   
TMDB popular순으로 모든 영화를 다 받아서, 배우랑 장르 관계도 추가하니 db가 11메가가 넘었다.   
fixture로 받아두기 위해, dumpdata를 시행하는데, 오류가 나서 저장이 중간에 멈췄다.   
구글링으로 검색하니, 아래와 같은 방법으로 하면 해결된다 해서 시행핬다.   
```py
#utf8로 dumpdata 만들기
python -Xutf8 ./manage.py dumpdata
```
이 방법은, 문제를 해결해줄 뿐만 아니라, utf로 변경하여 저장하여, 텍스트파일로 열어 다시 json으로 저장하는 번거로움을 덜어주기까지 한다.   