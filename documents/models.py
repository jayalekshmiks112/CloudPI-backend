from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_starred = models.BooleanField(default=False)

    def __str__(self):
        return self.name
