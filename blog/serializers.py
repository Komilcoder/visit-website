from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Profile


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','image','name','last_name')

    # def validate_image(self,image):
    #     file_size = image.file.size
    #     limit_kb = 150
    #     if file_size > limit_kb * 1024:
    #         raise ValidationError("Max size of file is %s KB  limit")



    def check_name(self,name,last_name):
        if not name or not last_name:
            raise ValidationError('Name or Last name must be provided')
        return name


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('image',)
                
        

