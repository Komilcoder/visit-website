from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
import jwt
import account
from rest_framework.authtoken.models import Token


class RegisterView(GenericAPIView):
    serializer_class = UserSerializers
    permission_classes = [AllowAny,]

    def post(self, request):
        serializers = UserSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = UserSerializers
    permission_classes = [AllowAny,]

    def post(self, request):
        data = request.data
        username = data.get('username','')
        password = data.get('password','')
        user = auth.authenticate(username=username, password=password)

        if user:
            payload = {
                'username':user.username,
                'password':user.password
            }
            auth_token = jwt.encode(payload," JWT_SECRET_KEY")

            serializer = UserSerializers(user)
            token, _ = Token.objects.get_or_create(user=user)
                            
            data = {
                'user': serializer.data,
                'token': token.key,
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response( status=status.HTTP_401_UNAUTHORIZED)
