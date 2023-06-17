from django.db import models



class Storage(models.Model):
    documents_percentage = models.FloatField(default=0)
    images_percentage = models.FloatField(default=0)
    music_percentage = models.FloatField(default=0)
    videos_percentage = models.FloatField(default=0)


