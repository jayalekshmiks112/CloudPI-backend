from django.urls import path
from . import views

app_name='images'

urlpatterns=[
    path('',views.image_view_upload,name='image_list'),
    path('<int:pk>/',views.image_delete,name='image_delete'),
    path('<int:pk>/add_to_starred/',views.add_to_starred,name='add-to-starred'),
]