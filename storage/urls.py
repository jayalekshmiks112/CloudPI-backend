from django.urls import path
from . import views

app_name = 'stored'

urlpatterns = [
    path('', views.storage_information),
    #path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('storage-info/',views.StorageInfoView.as_view(), name='storage-info'),
    
]
