from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Age# , Profile

class UserBaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)

class AgeSerializer(serializers.ModelSerializer):
    class human(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id',)

    user = human(write_only=True)

    class Meta:
        model = Age
        fields = ('id', 'user', 'age',)

class ProfileSerializer(serializers.ModelSerializer):
    # class User(serializers.ModelSerializer):
    #     class Meta:
    #         model = get_user_model()
    #         fields = ('id', )
    # user = User('user', read_only=True)
    followers_cnt = serializers.IntegerField(source='followers.count', read_only=True)
    followings_cnt = serializers.IntegerField(source='followings.count', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'followers_cnt', 'followings_cnt,', )# 'birth', 
