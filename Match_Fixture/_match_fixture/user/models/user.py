from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=300, unique=True, null=False)
    name = models.CharField(max_length=300, null=False)
    phone_num = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=100, null=False)
    otp_status = models.BooleanField(default=False)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone_num"]