from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65,min_length=8,write_only=True)
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']


    def validated(self,attrs):
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise ValidationError({'email':('Email is already in use')})
        return super().validated(attrs)

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


