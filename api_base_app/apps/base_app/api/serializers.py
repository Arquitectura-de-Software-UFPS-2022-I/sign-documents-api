from rest_framework import serializers
from apps.base_app.models import File, User, SignatureRequest, SignatureRequestUser

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
        extra_kwargs = {'uuid_image': {'required': False}}
        read_only_fields = ['uuid_image']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'username', 'email', 'password', 'signature']
        extra_kwargs = {'signature': {'required': False}}

class SignatureRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignatureRequest
        fields = '__all__'

class SignatureRequestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignatureRequestUser
        fields = '__all__'
        read_only_fields = ['signature_date']