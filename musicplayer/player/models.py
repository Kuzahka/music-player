from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255, blank=True)
    artist = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to="media")
    DJ = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mix',
        null=True
    )
