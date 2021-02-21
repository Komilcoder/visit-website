import jwt
from rest_framework import authentication,exceptions
from django.conf import settings
from django.contrib.auth.models import User

class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self,request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return None

        prefex,token = auth_data.decode('utf-8').split(' ')

        try:
            payload =jwt.decode(token,settings.JWT_SECRET_KEY)

            user = User.objects.get(username=payload['username'])
            return (user,token)

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Your Token is invalid,login')

        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Your Token is expired ,login')
            
        return super().authenticate(request)
