from django.urls import path
from . import views

app_name='videos'

urlpatterns=[
    path('',views.video_view_upload,name='video_list'),
    path('<int:pk>/',views.video_delete,name='video_delete'),
    path('<int:pk>/add_to_starred/',views.add_to_starred,name='add-to-starred'),
]