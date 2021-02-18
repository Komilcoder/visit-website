from django.contrib import admin
from .models import Profile


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('name','last_name')


admin.site.register(Profile,ProfilesAdmin)    