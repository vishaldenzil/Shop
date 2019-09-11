from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("User must have an email address")
        user_obj=  







# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(max_length =255,unique=True)
    staff = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
 
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    