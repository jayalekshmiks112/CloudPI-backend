import os
from rest_framework import serializers
from storage.models import Storage

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['documents_percentage', 'images_percentage', 'music_percentage', 'videos_percentage']

