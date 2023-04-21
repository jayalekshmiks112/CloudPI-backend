from django.urls import path
from . import views

app_name='documents'

urlpatterns=[
    path('',views.document_view_upload,name='document_list'),
    path('/<int:pk>/',views.document_delete,name='document_delete'),
    path('<int:pk>/add_to_starred/',views.add_to_starred,name='add-to-starred'),
]