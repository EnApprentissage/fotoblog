from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set', blank=True)

    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set', blank=True)

    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = [
        (CREATOR, 'Creator'),
        (SUBSCRIBER, 'Subscriber'),
    ]
    profile_photo = models.ImageField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
