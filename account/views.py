from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt


class RegisterView(GenericAPIView):
    serializer_class = UserSerializers
    def post(self, request):
        serializers = UserSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = UserSerializers

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)

            serializer = UserSerializers(user)
            data = {
                'user': serializer.data,
                'token': auth_token,
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid crediantials'}, status=status.HTTP_401_UNAUTHORIZED)
