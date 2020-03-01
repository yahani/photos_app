from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from photos.validator import photo_validator


class Photo(models.Model):
    image = models.ImageField(upload_to='images/', validators=[photo_validator])
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    saved = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.caption
