from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    avatar = models.ImageField(upload_to='users/',verbose_name='аватар', blank=True, null=True)
    phone = models.IntegerField(verbose_name='телефон', blank=True, null=True)
    country = models.CharField(max_length=150, verbose_name='страна', blank=True, null=True)
    confirmation_code = models.IntegerField(verbose_name='код верификации', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
