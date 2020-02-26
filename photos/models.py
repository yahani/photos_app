from django.db import models


# Create your models here.

class Photo(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
