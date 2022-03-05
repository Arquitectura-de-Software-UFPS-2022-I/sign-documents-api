import uuid
import os
from django.conf import settings
import base64

def handle_uploaded_file(image):
  
    file_name = uuid.uuid4().hex + '.png'
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    with open(file_path, 'wb+') as destination:
        destination.write(base64.b64decode(str(image)))

    return file_name
