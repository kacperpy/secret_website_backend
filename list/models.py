from django.db import models
import uuid


class Movie(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(
        max_length=69,
        unique=True
    )
    description = models.CharField(
        max_length=69,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
