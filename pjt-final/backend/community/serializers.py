from rest_framework import serializers
from .models import Review, Comment

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'created', 'updated',)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id','like_users', 'title', 'content', 'created', 'updated',)
        read_only_fields = ('like_users', )
class CommentSerializer(serializers.ModelSerializer):
    
            
    class Meta:
        model = Comment
        fields = ('id','content', 'created')