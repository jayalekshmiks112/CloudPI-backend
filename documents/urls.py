from django.urls import path
from . import views


app_name='documents'

urlpatterns=[
    path('upload/',views.document_view_upload,name='document_list'),
    path('<int:pk>/delete/',views.document_delete,name='document_delete'),
    path('<int:pk>/add_to_starred/',views.add_to_starred,name='add-to-starred'),
    path('starred_documents/', views.StarredDocumentListView.as_view(), name='star'),
    path('star/<int:id>/', views.StarredDocumentUpdateView.as_view(), name='stared'),


]

