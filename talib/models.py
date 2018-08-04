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


class Niveau(models.Model):
    description = models.TextField(max_length=1000)
    dawra = models.ForeignKey(
        'Dawra',
        on_delete = models.CASCADE
    )
class Dawra(models.Model):
    category = models.CharField(max_length=100)
    book     = models.ForeignKey(
        'Book',
         on_delete = models.CASCADE,
    )
    image = models.FileField(upload_to='image/',null=True,blank=True)
class Book(models.Model):
    title  = models.CharField(max_length=300)
    author = models.ForeignKey(
        'Author',
        on_delete = models.CASCADE,
    )
    edition = models.CharField(max_length=300)
    date = models.DateField()
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)