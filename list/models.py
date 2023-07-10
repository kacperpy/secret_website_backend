import uuid

from django.db import models


class Room(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=16
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    origin_room = models.ForeignKey(
        Room,
        related_name='movies',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=1028
    )
    description = models.CharField(
        max_length=512
    )
    description_long = models.CharField(
        max_length=2048
    )
    image_url = models.CharField(
        max_length=512
    )
    image_file = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
