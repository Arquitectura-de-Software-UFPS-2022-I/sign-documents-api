import os
from rest_framework.views import APIView
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from apps.base_app.models import File

class GetFileViewSet(APIView):
    def get(self, request, uuid_image):
        uuid_ext = uuid_image.split('.')
        uuid_img = uuid_ext[-1 if len(uuid_ext) < 2 else -2]
        file = File.objects.filter(uuid_image=uuid_img).first()
        ext = file.file.path.split('.')[-1].lower()
        
        content_type = 'application/pdf' if ext == 'pdf' else ('image/png' if ext == 'png' else 'image/jpg')
        image_file = open(file.file.path, 'rb')
        response = HttpResponse(FileWrapper(image_file), content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="%s"' % (file.name + '.' + ext)
        return response