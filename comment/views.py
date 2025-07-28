from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Comment, CommentHistory
from .serializers import CommentSerializer, CommentHistorySerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_update(self, serializer):
        old = self.get_object()
        CommentHistory.objects.create(comment=old, modified_by=self.request.user, old_text=old.text)
        serializer.save()

class CommentHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CommentHistory.objects.all()
    serializer_class = CommentHistorySerializer