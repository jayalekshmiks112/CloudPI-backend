from django.shortcuts import render
from rest_framework.response import Response

from documents.models import Document
from starred.models import StarredDocument

def index(request):
    starred_documents = StarredDocument.objects.all()

    context = {
        'starred_documents': starred_documents,
    }

    return Response(context)

def add_to_starred(request, document_id):
    document = Document.objects.get(id=document_id)

    if not document.is_starred:
        starred_document = StarredDocument(document=document)
        starred_document.save()

    return Response({'success': True})






