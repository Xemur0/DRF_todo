from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import User
# admin.site.register(User)


class CreateUsers(UserAdmin):
    list_display = ['username', 'first_name']

admin.site.register(User, CreateUsers)
