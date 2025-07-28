from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Permission
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'otp']

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        # Replace 'username' with 'email'
        credentials = {
            'email': attrs.get("email"),
            'password': attrs.get("password"),
        }

        user = authenticate(**credentials)

        if user is None:
            raise serializers.ValidationError("Invalid email or password")

        data = super().validate(attrs)
        data['user_id'] = user.id
        data['email'] = user.email
        return data