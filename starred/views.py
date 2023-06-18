from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from documents.models import Document
from images.models import Images
from videos.models import Videos
from music.models import Music

class StarredListView(APIView):
    def get(self, request):
        documents = Document.objects.filter(is_starred=True)
        images = Images.objects.filter(is_starred=True)
        videos = Videos.objects.filter(is_starred=True)
        music = Music.objects.filter(is_starred=True)

        
        response_data = {
            'documents': list(documents.values()),
            'images': list(images.values()),
            'videos': list(videos.values()),
            'music': list(music.values()),
        }

        return Response(response_data)

class StarredUpdateView(APIView):
    def put(self, request, app_label,id):
        model_map = {
            'documents': Document,
            'images': Images,
            'videos': Videos,
            'music': Music,
        }

        Model = model_map.get(app_label)
        if not Model:
            return Response({'detail': 'Invalid app label'}, status=400)

        item = get_object_or_404(Model, id=id)
        item.is_starred = not item.is_starred
        item.save()

        return Response({'detail': 'Item starred status updated successfully'})
