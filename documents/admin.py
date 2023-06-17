from django.contrib import admin


from .models import Document

import os

class DocumentAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        if obj.file:
            file_path = obj.file.path
            if os.path.exists(file_path):
                os.remove(file_path)
        super().delete_model(request, obj)

admin.site.register(Document, DocumentAdmin)
