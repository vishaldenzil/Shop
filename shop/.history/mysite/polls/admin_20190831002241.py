from django.contrib import admin
from .models import User
from django.contrib.auth import get_user_model

User

# Register your models here.

admin.site.register(User)