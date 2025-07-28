from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, CommentHistoryViewSet

router = DefaultRouter()
router.register('comments', CommentViewSet)
router.register('history', CommentHistoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]