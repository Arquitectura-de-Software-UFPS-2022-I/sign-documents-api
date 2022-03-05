from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import views
from .serializers import ValidateSerializer
from .validate_signature import ClassifierSignature
from .processing_image import handle_uploaded_file
# Create your views here.

class ValidateSignatureView(views.APIView):
    classifier = ClassifierSignature()

    def post(self, request: Request):
    
        file_name = handle_uploaded_file(request.data['image'])
        result = ValidateSerializer(self.classifier.validate_image(file_name)).data

        return Response(result)
        