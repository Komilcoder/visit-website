from rest_framework import serializers   
from django.core.exceptions import ValidationError
from .models import MediaSource
from rest_framework.fields import FileField



class MediaSourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaSource
        fields = ('id','title','video','description','created')
    

class MultipleFileUploadSerializer(serializers.Serializer):
    video = serializers.ListField(FileField())
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    created = serializers.DateTimeField()
    