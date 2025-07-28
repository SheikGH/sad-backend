from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Permission
from .serializers import UserSerializer, CreateUserSerializer, PermissionSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import EmailTokenObtainPairSerializer
import random
import logging

# Create your views here.
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    logger = logging.getLogger("TESTING")
    logger.debug('UserViewSet')

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def create_user(self, request):
        logger.debug(f'POST Data is {request} {request.data}')
        email = request.data.get('email')
        username = email.split('@')[0]
        password = User.objects.make_random_password()
        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({'email': email, 'password': password})

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def send_otp(self, request):
        email = request.data['email']
        user = User.objects.get(email=email)
        otp = str(random.randint(100000, 999999))
        user.otp = otp
        user.save()
        send_mail('Password Reset OTP', f'Your OTP is {otp}', 'noreply@app.com', [email])
        return Response({'status': 'OTP sent'})

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def reset_password(self, request):
        email = request.data['email']
        otp = request.data['otp']
        new_password = request.data['new_password']
        user = User.objects.get(email=email, otp=otp)
        user.set_password(new_password)
        user.otp = ''
        user.save()
        return Response({'status': 'Password reset successful'})

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer