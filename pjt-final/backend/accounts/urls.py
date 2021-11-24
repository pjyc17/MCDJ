from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    ###유저확인###
    path('user/', views.user),

    path('<int:user_pk>/follow/', views.follow),
    path('birthday/', views.birthday),
    ###profile###
    path('<int:user_id>/', views.profile),
]
### 아이디를 만들 url 생성하고 -> views.py 생성 ###
### 프로필 유저의 id, username, birthday(year) ###