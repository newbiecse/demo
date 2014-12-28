from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
