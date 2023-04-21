from django.urls import path
from . import views

urlpatterns = [
    path('serach/', views.search_files, name='search-files'),
    path('recent/',views.recently_added_files,name='recent-files'),
    
]
