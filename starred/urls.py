# starred/urls.py
from django.urls import path
from .views import StarredListView, StarredUpdateView

app_name = 'starred'

urlpatterns = [
    path('', StarredListView.as_view(), name='list'),
    path('<str:app_label>/<int:id>/', StarredUpdateView.as_view(), name='update'),
]
