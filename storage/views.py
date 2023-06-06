from rest_framework.decorators import api_view
from rest_framework.response import Response
from storage.models import Storage
from storage.serializers import StorageSerializer
from documents.models import Document
from images.models import Images
from music.models import Music
from videos.models import Videos

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
