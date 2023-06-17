from django.contrib import admin

# Register your models here.
from .models import StarredDocument

admin.site.register(StarredDocument)