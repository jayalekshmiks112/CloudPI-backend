
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import File
from .serializers import FileSerializer

class UploadFileView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class DeleteFileView(APIView):
    def delete(self, request, id):
        try:
            file = File.objects.get(id=id)
            file.delete()
            return Response({'message': 'File deleted successfully.'})
        except File.DoesNotExist:
            return Response({'message': 'File not found.'}, status=404)

class RetrieveFileView(APIView):
    def post(self, request):
        try:
            file = File.objects.get(id=request.data['id'])
            return Response({'file': file.file.url})
        except File.DoesNotExist:
            return Response({'message': 'File not found.'}, status=404)
