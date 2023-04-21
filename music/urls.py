from django.urls import path
from . import views

app_name='music'

urlpatterns=[
    path('',views.music_view_upload,name='music_list'),
    path('/<int:pk>/',views.music_delete,name='music_delete'),
    path('<int:pk>/add_to_starred/',views.add_to_starred,name='add-to-starred'),
]