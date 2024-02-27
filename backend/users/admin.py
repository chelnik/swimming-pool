from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'age',
                    'is_staff', 'last_login', 'date_joined', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
