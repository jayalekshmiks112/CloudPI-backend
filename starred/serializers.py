# starred/serializers.py
from rest_framework import serializers
from .models import Starred

class StarredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starred
        fields = '__all__'


"""
from rest_framework import serializers
from documents.serializers import DocumentSerializer
from music.serializers import MusicSerializer
from videos.serializers import VideoSerializer
from images.serializers import ImageSerializer
from .models import Starred

class StarredSerializer(serializers.ModelSerializer):
    document = DocumentSerializer(read_only=True)
    music = MusicSerializer(read_only=True)
    video = VideoSerializer(read_only=True)
    image = ImageSerializer(read_only=True)

    class Meta:
        model = Starred
        fields = ['document', 'music', 'video', 'image']
"""