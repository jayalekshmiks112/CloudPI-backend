from django.urls import path
from storage.views import storage_information

urlpatterns = [
    path('', storage_information),
    
]
