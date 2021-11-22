from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Birthday


class UserBaseSerializer(serializers.ModelSerializer):
    class UserBirthday(serializers.ModelSerializer):
        class Meta:
            model = Birthday
            fields = ('id', 'birthday',)
    birthday = UserBirthday('birthday', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'birthday',)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)

class BirthdaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Birthday
        fields = ('id', 'birthday',)

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
        fields = ('id', 'username', 'followers_cnt', 'followings_cnt', )# 'birth', 
