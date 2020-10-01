from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
  username = models.CharField(max_length=200, unique=True)

class Blogpost(models.Model):
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=200)
  content = models.TextField()
  summary = models.TextField()
  image = models.CharField(max_length=200)
  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  published_date = models.DateTimeField('date published')
