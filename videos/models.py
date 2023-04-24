from django.db import models

class Videos(models.Model):
    name=models.CharField(max_length=200)
    video=models.FileField(upload_to='videos/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    is_starred=models.BooleanField(default=False)

    def __str__(self):
        return self.name