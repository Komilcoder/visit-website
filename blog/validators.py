import os
# import magic
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from visitapp import settings


# def validate_file_type(upload):
#     # Make uploaded file accessible for analysis by saving in tmp
#     valid_mime_types = ['application/jpg','application/jpeg','application/png','application/mp4']
#     tmp_path = 'tmp/%s' % upload.name[2:]
#     default_storage.save(tmp_path, ContentFile(upload.file.read()))
#     full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)

#         # Get MIME type of file using python-magic and then delete
#     file_type = magic.from_file(full_tmp_path, mime=True)
#     default_storage.delete(tmp_path)

#     if file_type not in settings.IMAGE_TYPES and file_type not in settings.VIDEO_TYPES:
#         raise ValidationError('File type not supported. JPEG, PNG,JPG or MP4 recommended.')
   

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')   
