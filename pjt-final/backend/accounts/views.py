from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ProfileSerializer, UserSerializer, UserBaseSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password2 = request.data.get('password2')
    if password != password2:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def user(request):
    serializer = UserBaseSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def profile(request, user_id):
    person = get_object_or_404(get_user_model(), pk=user_id)
    print(person)
    print('########')
    print('########')
    print('########')
    print('########')
    print('########')
    print('########')
    print('########')
    print('########')
    print('########')
    print('########')
    print('########')
    serializer = ProfileSerializer(data=person)
    print('########')
    print(serializer.data)
    return Response(serializer.data)

# def follow(request, user_pk):
#     person = get_object_or_404(get_user_model(), pk=user_pk)
#     if person.followers.filter(pk=request.user.pk).exists():
#         person.followers.remove(request.user)
#     else:
#         person.followers.add(request.user)
#     return
        
    