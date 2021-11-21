from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_create),
    path('all/', views.all),
    path('<int:review_id>/', views.review_detail_update_delete),
    path('<int:review_id>/comment/', views.comment),
    path('comment/<int:comment_id>/', views.delcom),
    # path('<int:review_pk>/like/', views.like, name='like'),
]