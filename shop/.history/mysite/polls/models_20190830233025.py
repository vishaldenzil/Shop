from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
# Create your models here.
class User(AbstractBaseUser):
    email = models.EmaIlField(max_length =255,unique=True)
    staff = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    admin = 
    pass