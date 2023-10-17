from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from djshop.auths.users.models import User


# Register your models here.

@admin.register(User)
class DjshopUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "verified_email")