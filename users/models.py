from django.contrib.auth.models import AbstractUser
from django.db import models

from list.models import Room


class CustomUser(AbstractUser):
    room = models.ForeignKey(
        Room,
        related_name='members',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
