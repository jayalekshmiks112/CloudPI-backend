from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Videos
from .serializers import VideoSerializer

@api_view(['GET', 'POST'])
def video_view_upload(request):
    if request.method == 'GET':
        video= Videos.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def video_delete(request, pk):
    try:
        video = Videos.objects.get(pk=pk)
    except Videos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        is_starred = video.is_starred
        video.delete()

        if is_starred:
            starred = request.user.starred_documents.all()
            if video in starred:
                request.user.starred_documents.remove(video)

        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def add_to_starred(request, pk):
    try:
        video = Videos.objects.get(pk=pk)
    except Videos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    request.user.starred_documents.add(video)

    return Response(status=status.HTTP_204_NO_CONTENT)

