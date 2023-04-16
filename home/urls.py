from django.urls import path
from .views import UploadFileView, DeleteFileView, RetrieveFileView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload'),
    path('delete/<int:id>/', DeleteFileView.as_view(), name='delete'),
    path('retrieve/', RetrieveFileView.as_view(), name='retrieve'),
]
