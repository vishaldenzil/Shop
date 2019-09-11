from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
# Create your models here.
class User(AbstractBaseUser):
    email = models.EmaIlField(max_length =255,unique=True)
    staff = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
 
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email

    def get_full_name(self):
        return self.email