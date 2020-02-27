from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
