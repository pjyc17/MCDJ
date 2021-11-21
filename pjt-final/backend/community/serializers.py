from rest_framework import serializers
from .models import Review, Comment
from django.contrib.auth import get_user_model

class ReviewListSerializer(serializers.ModelSerializer):
    class User(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')
            read_only_fields = ('username',)
    user = User('user')
    likes_cnt = serializers.IntegerField(source='like_users.count')
    reviews_cnt = serializers.IntegerField(source='comments.count')
    class Meta:
        model = Review
        fields = ('id', 'user', 'likes_cnt', 'reviews_cnt', 'title', 'content', 'created', 'updated',)
        read_only_fields = ('likes_cnt', 'reviews_cnt',)

class ReviewSerializer(serializers.ModelSerializer):
    class User(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username',)
            # read_only_fields = ('username',)
    class CommentSerializer(serializers.ModelSerializer):
        class User(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username',)
        user = User('user', read_only=True)
        class Meta:
            model = Comment
            fields = ('id', 'content', 'user', 'created',)

    user = User('user', read_only=True)
    likes_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
    comments = CommentSerializer('comments', many=True, read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'user', 'likes_cnt', 'title', 'content', 'created', 'updated', 'comments',)
        # read_only_fields = ('user', 'likes_cnt')


class CommentSerializer(serializers.ModelSerializer):
    class User(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username',)
    user = User('user', read_only=True)
    class Meta:
        model = Comment
        fields = ('id','content', 'created', 'user',)