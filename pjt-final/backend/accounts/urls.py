from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('user/', views.user),
    path('<int:user_id>/', views.profile),
    path('birthday/', views.birthday),
    path('<int:user_pk>/follow/', views.follow),
]