from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list_create),
    path('<int:review_pk>/', views.review_update_delete),
    path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),
    # path('<int:review_pk>/like/', views.like, name='like'),
]
