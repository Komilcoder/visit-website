from django.contrib import admin
from .models import MediaSource

class MediasAdmin(admin.ModelAdmin):
    list_display = ('user','description','created')

admin.site.register(MediaSource,MediasAdmin)    