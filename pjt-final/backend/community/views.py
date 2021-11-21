from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import ReviewSerializer, CommentSerializer, ReviewListSerializer
from .models import Review, Comment


@api_view(['POST'])
def review_create(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def all(request):
    reviews = Review.objects.all().order_by('-created')
    if reviews:
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        return Response({})

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def review_detail_update_delete(request, review_id):
    review = Review.objects.get(pk=review_id)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.user == review.user: 
        if request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            review.delete()
            return Response({'id': review_id})
    return Response({})


# 리뷰 항목의 comment 를 review의 것임을 확인하고 comment 달아주는 작업이 진행이 잘 안됨
@api_view(['POST'])
def comment(request, review_id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        review = get_object_or_404(Review, pk=review_id)
        serializer.save(user=request.user, review=review)
        return Response(serializer.data)
        
@api_view(['DELETE'])
def delcom(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user:
        comment.delete()
    return Response({'message': '삭제했다잉'})


@api_view(['GET', 'PUT'])
def like(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'GET':
        if review.like_users.filter(pk=request.user.pk).exists():
            isLiked = True
        else:
            isLiked = False
    else:
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            isLiked = False
        else:
            review.like_users.add(request.user)
            isLiked = True
    return Response({'isLiked': isLiked, 'likes_cnt': review.like_users.count()})