from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from .models import MediaSource
from .serializers import (
    MediaSourcesSerializer,
    MultipleFileUploadSerializer,

)    
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
# from blog.models import Profile
# from blog.serializers import ProfileSerializers,ProfileImageSerializer
from django.http import Http404
User = get_user_model()


class MediaSourceList(APIView):
    """ GET,POST methos:
    
    title = title,
    video = video url,
    description = description
    """
    permission_classes = [AllowAny,]

    def get(self,request,format=None):
        media = MediaSource.objects.all().order_by('-created')
        serializer = MediaSourcesSerializer(media,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = MediaSourcesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    
class MediaSourceDetailView(APIView):
    """ Retreive,PUT,DELETE methods:
        title = title,
        video = video url,
        description = description
     """

    permission_classes = [AllowAny,]

    def get_object(self,pk):
        try:
            return MediaSource.objects.get(pk=pk)
        except MediaSource.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        query = self.get_object(pk)
        serializer = MediaSourcesSerializer(query)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        media = self.get_object(pk)
        serializer = MediaSourcesSerializer(media,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 




    
        




