from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Images
from .serializers import ImageSerializer

@api_view(['GET', 'POST'])
def image_view_upload(request):
    if request.method == 'GET':
        image = Images.objects.all()
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def image_delete(request, pk):
    try:
        image = Images.objects.get(pk=pk)
    except Images.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        is_starred = image.is_starred
        image.delete()

        if is_starred:
            starred = request.user.starred_documents.all()
            if image in starred:
                request.user.starred_documents.remove(image)

        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def add_to_starred(request, pk):
    try:
        image = Images.objects.get(pk=pk)
    except Images.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    request.user.starred_documents.add(image)

    return Response(status=status.HTTP_204_NO_CONTENT)
