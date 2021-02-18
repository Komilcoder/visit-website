from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField, 
    FileField, 
    ListField,
    DateTimeField
)   
from django.core.exceptions import ValidationError
from .models import MediaSource




class MediaSourceSerializer(Serializer):
    file_type = FileField()
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    created = DateTimeField()
    updated = DateTimeField()

    

class MultipleFileUploadSerializer(Serializer):
    file_type = ListField(FileField())
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    created = DateTimeField()
    updated = DateTimeField()

