from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from django.utils import timezone

@api_view(['GET'])
def search_files(request, query):
    file_serached = File.objects.filter(name__icontains=query)
    serializer = FileSerializer(file_serached, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def recently_added_files(request):
    recent_files = File.objects.filter(created_at__gte=timezone.now()-timezone.timedelta(days=7)).order_by('-created_at')
    serializer = FileSerializer(recent_files, many=True)
    return Response(serializer.data)
