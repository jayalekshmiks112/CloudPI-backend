from rest_framework.decorators import api_view
from rest_framework.response import Response
from storage.models import Storage
from storage.serializers import StorageSerializer
from documents.models import Document
from images.models import Images
from music.models import Music
from videos.models import Videos
from rest_framework.views import APIView
from django.core.files.storage import default_storage

from .utils import get_storage_info


@api_view(['GET'])
def storage_information(request):
    documents_count = Document.objects.count()
    images_count = Images.objects.count()
    music_count = Music.objects.count()
    videos_count = Videos.objects.count()

    total_count = documents_count + images_count + music_count + videos_count

    documents_percentage = (documents_count / total_count) * 100 if total_count > 0 else 0
    images_percentage = (images_count / total_count) * 100 if total_count > 0 else 0
    music_percentage = (music_count / total_count) * 100 if total_count > 0 else 0
    videos_percentage = (videos_count / total_count) * 100 if total_count > 0 else 0

    storage = Storage(
        documents_percentage=documents_percentage,
        images_percentage=images_percentage,
        music_percentage=music_percentage,
        videos_percentage=videos_percentage
    )
    serializer = StorageSerializer(storage)
    return Response(serializer.data)
"""
class FileUploadView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        file_size = file.size / (1024 ** 3)  

        if file_size > get_storage_info()['remaining_storage']:
            return Response({'detail': 'Not enough storage capacity.'})

        file_path = default_storage.save(file.name, file)

        file_obj = File(name=file.name, size=file_size)
        file_obj.save()

        serializer = FileSerializer(file_obj)
        return Response(serializer.data)
"""

class StorageInfoView(APIView):
    def get(self, request):
        storage_info = get_storage_info()
        return Response(storage_info)