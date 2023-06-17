from django.db import models
from django.contrib.auth.models import User

class Locked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mail = models.EmailField()
    otp = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.mail} - {self.user.username}"
