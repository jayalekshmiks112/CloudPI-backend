from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Document
from .serializers import DocumentSerializer

@api_view(['GET', 'POST'])
def document_view_upload(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def document_delete(request, pk):
    try:
        document = Document.objects.get(pk=pk)
    except Document.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        is_starred = document.is_starred
        document.delete()

        if is_starred:
            starred = request.user.starred_documents.all()
            if document in starred:
                request.user.starred_documents.remove(document)

        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def add_to_starred(request, pk):
    try:
        document = Document.objects.get(pk=pk)
    except Document.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    request.user.starred_documents.add(document)

    return Response(status=status.HTTP_204_NO_CONTENT)
