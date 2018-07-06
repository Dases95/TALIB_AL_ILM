from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    #create relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #add any additional attrebutes you want
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.user.username