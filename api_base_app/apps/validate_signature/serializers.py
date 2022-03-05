from rest_framework import serializers

class ValidateSerializer(serializers.Serializer):
    class_label = serializers.IntegerField()
    confidence = serializers.FloatField()