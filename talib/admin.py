from django.contrib import admin
from talib.models import UserProfileInfo
from . import models
admin.site.register(UserProfileInfo)
admin.site.register(models.Book)
admin.site.register(models.Dawra)
admin.site.register(models.Author)
admin.site.register(models.Niveau)