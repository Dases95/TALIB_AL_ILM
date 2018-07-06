from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    #create relationship
    user = models.OneToOneField(User)
    #add any additional attrebutes you want
    country = models.CharField(blank=True)
    def __str__(self):
        return self.user.username