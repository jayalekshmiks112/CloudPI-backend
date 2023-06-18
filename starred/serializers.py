# starred/serializers.py
from rest_framework import serializers
from .models import Starred

class StarredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starred
        fields = '__all__'
