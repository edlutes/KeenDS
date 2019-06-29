from .models import File, Row
from rest_framework import serializers

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = "__all__"