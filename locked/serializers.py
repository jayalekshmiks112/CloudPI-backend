from rest_framework import serializers
from .models import Locked

class LockedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locked
        fields = ['mail', 'otp']


