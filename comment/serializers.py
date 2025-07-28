from rest_framework import serializers
from .models import Comment, CommentHistory

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentHistory
        fields = '__all__'