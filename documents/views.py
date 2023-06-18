from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Document
#import os
from .serializers import DocumentSerializer
from rest_framework.parsers import MultiPartParser,FormParser
from starred.models import Starred

#from django.conf import settings
#from django.core.files.storage import default_storage



@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser,FormParser])
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
        file_path=document.file.path
        #print(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
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

    if document.is_starred:
        starred_document=Starred.objects.get(document=document)
        starred_document.delete()
    else:
        starred_document = Starred(document=document)
        starred_document.save()

    document.is_starred = not document.is_starred
    document.save()

    return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import generics

from .models import Document
from .serializers import DocumentSerializer


class StarredDocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        queryset = Document.objects.filter(is_starred=True)
        return queryset

class StarredDocumentUpdateView(generics.UpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    lookup_field = 'id'
    allowed_methods = ['PUT']

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        is_starred = instance.is_starred

        instance.is_starred = not is_starred
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
