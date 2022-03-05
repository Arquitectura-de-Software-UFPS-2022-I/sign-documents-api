import os, uuid, fitz

from ..models import File, User, SignatureRequest, SignatureRequestUser
from .serializers import FileSerializer, SignatureRequestSerializer, SignatureRequestUserSerializer, UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.conf import settings
from wsgiref.util import FileWrapper

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        ext = self.request.data['file'].name.split(".")[-1]
        uuid_image = str(uuid.uuid4())
        self.request.data['file'].name = uuid_image + '.' + ext
        serializer.save(uuid_image=uuid_image)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

class SignatureRequestViewSet(viewsets.ModelViewSet):
    queryset = SignatureRequest.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = SignatureRequestSerializer

class SignatureRequestUserViewSet(viewsets.ModelViewSet):
    queryset = SignatureRequestUser.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = SignatureRequestUserSerializer

class ListSignatureRequestByUserViewSet(APIView):
    def get(self, request, user_id):
        data = SignatureRequest.objects.filter(user_id = user_id)
        signature_request_serializer = SignatureRequestSerializer(data, many=True)
        return Response(signature_request_serializer.data)

class ListSignatureRequestUserByUserViewSet(APIView):
    def get(self, request, user_id):
        data = SignatureRequestUser.objects.filter(user_id=user_id)
        signature_request_user_serializer = SignatureRequestUserSerializer(data, many=True)
        return Response(signature_request_user_serializer.data)

class ListSignatureRequestUserByRequestViewSet(APIView):
    def get(self, request, request_id):
        data = SignatureRequestUser.objects.filter(request_id=request_id)
        signature_request_user_serializer = SignatureRequestUserSerializer(data, many=True)
        return Response(signature_request_user_serializer.data)

class GetGenerateFileSignedFromRequestSignature(APIView):
    def get(self, request, request_id) -> bytes:
        signature_request_users = SignatureRequestUser.objects.filter(request_id=request_id, signed=True).all()
        signature_request = SignatureRequest.objects.filter(id=request_id).first()
        
        file_handle = fitz.open(signature_request.document.file.path)
        for signature_request_user in signature_request_users:

            signature = open(signature_request_user.user.signature.file.path, "rb").read()

            image_rectangle = fitz.Rect(
                signature_request_user.pos_x, 
                signature_request_user.pos_y, 
                signature_request_user.pos_x+100,
                signature_request_user.pos_y+100
            )

            num_page = file_handle[signature_request_user.num_page-1]
            num_page.insert_image(image_rectangle, stream=signature)

        path_pdf = os.path.join(os.path.join(settings.MEDIA_ROOT, 'files'), str(uuid.uuid4())+'.pdf')
        file_handle.save(path_pdf)
        file_handle.close()

        image_file = open(path_pdf, 'rb')
        response = HttpResponse(FileWrapper(image_file), content_type='application/pdf')

        image_file.close()
        os.remove(path_pdf)

        response['Content-Disposition'] = 'attachment; filename="%s"' % (signature_request.document.name+'.pdf')
        return response
