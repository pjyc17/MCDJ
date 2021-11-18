> 날짜별 정리

# 11.16

- 기본 설정들 allauth, cors, jwt 적용   

---

---



# 11.17 (첫 날)

### [MCDJ 로고](https://www.wix.com/logo/maker/esh/zoe-templates?companyName=mcdj&industry=%7B%22industry%22%3A%22dd%22%2C%22isCustom%22%3Atrue%7D&tags=dynamic%2Cfun%2Ccreative&logoPurpose=website&tid=3ba5f5c3-f513-482c-80fe-7f9a2bb19d96&referralAdditionalInfo=arenaSplitPage) & [favicon 제작](https://realfavicongenerator.net/)   

![image-20211118003942045](README.assets/image-20211118003942045.png)



- ![img](README.assets/MCDJ3.png)



### 강아지 움짤 제작   

- ![0ce2544f72f6f66c](README.assets/0ce2544f72f6f66c-16371635188582.gif)



### 배경 디스코드 채팅색 적용   

- colorcop 이용 (#36393f)



### 로그인, 로그아웃, 회원가입 적용

- google로그인 새창띄움했지만, 오류가 있음 -> 뷰의 부트스트랩을 다운... 
- bootstrap모달 적용했지만  
- 모달의 우상단 종료버튼의 표시가 무척이나 마음에 들지 않아 변경하고자 했으나 찾지못함...
- 아마 뷰의 부트스트랩 설정이 완벽하지 않은 문제이지 싶음 -> 직접 만들계획(설정을 변경하는게 쉽지 않아)

![image-20211118004037067](README.assets/image-20211118004037067.png)



### ERD 모델링 하기

- 메인으로 생각하는 유저의 생일과 영화의 RELEASED_DATE 부분의 연결에 고민시간이 더 필요

![ERD초안작성_그림만](README.assets/ERD초안작성_그림만-16371451478045-16371635277463.png)

### 메인화면, 디테일 페이지 디자인

- [오븐앱](https://ovenapp.io/project/eEgZ5ttZEIHDDRNGGpS5BmVg7jG6fLzF#BXMku) 을 이용한 간단한 페이지 디자인 제작
- 넷플릭스, 왓챠, 웨이브 등의 경쟁사 벤치마킹
- 와챠와 넷플릭스를 보며 주제에 맞게 변경, 디자인

![image-20211118003714530](README.assets/image-20211118003714530-16371635310924.png)

![image-20211118003730984](README.assets/image-20211118003730984-16371635332875.png)

![image-20211118003742705](README.assets/image-20211118003742705-16371635355206.png)

![image-20211118003757231](README.assets/image-20211118003757231-16371635380297.png)

### django accounts/models.py 초안 작성  

- accouts/models.py

```
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

class Age(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='age')
    age = models.PositiveIntegerField()
```

- community/models.py

```
from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"title : {self.title}"

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

```

- movies/models.py

```
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    released_date = models.DateField()
    poster_path = models.TextField
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    popularity = models.FloatField()

    def __str__(self):
        return f'title : {self.title}'

class Genre(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='genres')

class Actor(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='actors')
    
    def __str__(self):
        return f'name: {self.name}'

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.movie_id}, {self.title}'
```

### 모델을 작성하며 변경한 ERD 모델링

![image-20211118032407938](README.assets/image-20211118032407938-16371734533191.png)

### 리드미 작성 및 계획 수립

- 주윤아 오늘도 수고 많았어 ㅎㅎ 아마 동유 오면 이 글을 발견하고 몹시 화가 날 수 있지만 그래도 오늘 고생했으니 나에게 주는 선물은 꿀잠이라고 할 수 있지 모델을 작성하기로 했는데 정말 쉽지 않다..
- 혼날 것 같으니 내일 할 일에 대해 적어보자면 아마 모델링 한 부분에 대한 모델을 작성하고 
- 장고 뷰부분을 작성하고 우리 최대 난관이자 프로젝트의 가장 핵심이 되는 생일관련 이슈를 해결할 것이다.
- 생일정보를 유저에 포함시키려다 보니 createsuperuser생성에도 문제가 생긴다고...

![image-20211118004601761](README.assets/image-20211118004601761.png)

- 모델링 하면서 RANK 에서 별점을 메겨주기 위해서 추가적으로 아래와 같이 넣어주자~~!!

![img](README.assets/django1022_1.JPG)

---

---

# 11.18

## 오늘의 할일 - 계획

- 영화데이터에서 serializer 사용해서 데이터 받아오기(pjt08, pjt02 확인)
- ![image-20211118102804650](C:\Users\pjyc1\AppData\Roaming\Typora\typora-user-images\image-20211118102804650.png)
- 데이터 받아온 것 app.vue 에서 뿌려주기

장르테이블 - 장르 아이디 장르이름 

영화테이블 - 영화 아이디 영화이름 장르아이디

# design

- 메인페이지 만들기(날짜 유저한테 넣어주는거 해주세요)

---

### 어제 models.py 수정본

- community movies 의 review 기능중 rank ★ 를 작성해주기
  - (like follow comment 커뮤니티 기능구현)

```
class Review(models.Model):
    RANKS = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"title : {self.title}"
```

- 위와 같이 변경하던 중 발견한 movies 의 models.py 에서 rank는 무의미함을 발견하고 수정

