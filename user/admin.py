# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(DefaultUserAdmin):
    # Optional: customize display
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'is_super_admin')
    # list_filter = ('is_active', 'is_staff', 'is_superuser')
    # search_fields = ('username', 'email')
