from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

import os
from uuid import uuid4


def get_profile_image_path(instance, filename):
    ext = str(filename).split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return os.path.join('profile/pictures/', filename)




class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to=get_profile_image_path)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user) + str(self.name)


