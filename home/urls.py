"""
from django.urls import path
#from .views import upload_file, delete_file

from . import views
app_name='home'

urlpatterns = [
    #path('',views.home, name='home'),
    path('upload/', views.upload_file.as_view(), name='upload'),
    path('delete/<int:file_id>/', views.delete_file.as_view(), name='delete'),
]
"""
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import FileViewSet, home, upload_file, delete_file

router = routers.DefaultRouter()
router.register(r'files', FileViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_file, name='upload'),
    path('delete/<int:file_id>/', delete_file, name='delete'),
    url(r'^api/', include(router.urls)),
]
