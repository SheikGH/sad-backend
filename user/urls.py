from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PermissionViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('permissions', PermissionViewSet, basename='permission')

urlpatterns = [
    path('', include(router.urls))
]