from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_create),
    path('all/', views.all),
    path('<int:review_id>/', views.review_detail_update_delete),
    path('<int:review_id>/comment/', views.comment),
    path('comment/<int:comment_id>/', views.delcom),
    path('<int:review_id>/like/', views.like),

    ###프로필###
    path('review/<int:user_id>/', views.review),
    path('liked_review/<int:user_id>/', views.liked_review),
]