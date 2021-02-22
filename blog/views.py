from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import (
    ProfileSerializers,
    ProfileImageSerializer,
)
from django.http import Http404
from rest_framework import viewsets

class ProfileList(APIView):
    """ 
       get,post method:
      user = user,
      image = image,
      name = first_name,
      last_name=last_name
    """

    permission_classes = [AllowAny,]

    def get(self,request,format=None):
        query = Profile.objects.all()
        serializer = ProfileSerializers(query,many = True)
        return Response(serializer.data)

    def post(self,request,format=None):
        post = request.POST
        if not post:
            raise ValidationError('Something went wrong')

        serializer = ProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

   
class ProfileDetailView(APIView):
    """ POST,Retreive,delete:
        user = username,
        image = image,
        name = name,
        last_name=last_name
    
    """

    def get_object(self,pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        query = self.get_object(pk)
        serializer = ProfileSerializers(query)
        return Response(serializer.data)

    def put(self,request,pk,format=None):

        query = self.get_object(pk)
        serializer = ProfileSerializers(query,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONT)        




class ProfileListImageView(APIView):
    """here:only for image, list image
        GET method
        image= image
    """

    def get(self,request,format=None):
        profile = Profile.objects.get(id=1)
        serializer = ProfileImageSerializer(profile)
        print(serializer)
        return Response(serializer.data)


class ProfileImageView(APIView):
    """ here:only for image,retreive,update,delete 
    POST method
    image = image
    
    """ 

    def get_object(self,pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def patch(self,request,pk,format=None):
        data = request.data
        user = request.user.id
        profile = self.get_object(pk)
        data['user'] = user
        serializer = ProfileImageSerializer(profile,data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

    def get(self,request,pk,format=None):
        profile = self.get_object(pk)
        serializer = ProfileImageSerializer(profile)
        return Response(serializer.data)

    def delete(self,request,pk,format=None):
        profile = self.get_object(pk)
        print(profile)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








