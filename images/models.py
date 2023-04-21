from django.db import models

class Images(models.Model):
    title=models.CharField(max_length=200)
    image=models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title