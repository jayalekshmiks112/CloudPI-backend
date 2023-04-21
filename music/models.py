from django.db import models

class Music(models.Model):
    title= models.CharField(max_length=200)
    music=models.FileField(upload_to='music/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title