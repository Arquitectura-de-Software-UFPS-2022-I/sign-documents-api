from ..models import File, User, SignatureRequest, SignatureRequestUser
from .serializers import FileSerializer, SignatureRequestSerializer, SignatureRequestUserSerializer, UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = FileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

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
        signature_request_serializer = SignatureRequestSerializer(data, many=True)
        return Response(signature_request_serializer.data)

class ListSignatureRequestUserByRequestViewSet(APIView):
    def get(self, request, request_id):
        data = SignatureRequestUser.objects.filter(request_id=request_id)
        signature_request_serializer = SignatureRequestSerializer(data, many=True)
        return Response(signature_request_serializer.data)