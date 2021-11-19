from rest_framework import serializers
from .models import Review, Comment

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id','like_users', 'title', 'content', 'created', 'updated', 'rank',)
        read_only_fields = ('like_users', )
class CommentSerializer(serializers.ModelSerializer):
    
            
    class Meta:
        model = Comment
        fields = ('id','content', 'created')