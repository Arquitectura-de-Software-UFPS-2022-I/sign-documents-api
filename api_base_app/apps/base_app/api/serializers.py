from rest_framework import serializers
from apps.base_app.models import File, User, SignatureRequest, SignatureRequestUser

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

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