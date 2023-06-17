from django.urls import path

from .views import index, add_to_starred

urlpatterns = [
    path('', index, name='index'),
    path('add_to_starred/<int:document_id>', add_to_starred, name='add_to_starred'),
]

