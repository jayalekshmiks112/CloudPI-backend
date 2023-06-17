from django.db import models

class StarredDocument(models.Model):
    document = models.ForeignKey('documents.Document', on_delete=models.CASCADE)



