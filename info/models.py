from django.db import models

from django.contrib.auth import get_user_model
import os
from uuid import uuid4
from .validators import validate_file_extension 

User = get_user_model()


def get_profile_image_path(instance, filename):
    ext = str(filename).split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return os.path.join('profile/media/', filename)


def image_path(instance, filename):
    ext = str(filename).split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return os.path.join('profile/pictures/', filename)



class MediaSource(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=255,null=True)
    video = models.FileField(upload_to=get_profile_image_path,validators=[validate_file_extension],null=True)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + str(self.created)

    def count_files(self):
        return self.video.count()  

    @property
    def filesize(self):
        x = self.video
        y = 512000
        if x < y:
            value = round(x/1000,2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000,2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value)+ext
                          
