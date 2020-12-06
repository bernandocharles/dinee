from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Blogpost(models.Model):
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=200)
  content = models.TextField()
  summary = models.TextField()
  image = models.CharField(max_length=200)
  author = models.CharField(max_length=200, default="dineeAdmin")
  category = models.CharField(max_length=200, default="pelanggan")

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  published_date = models.DateTimeField('date published')

class Question(models.Model):
  question = models.CharField(max_length=200)
  answer = models.TextField()
  category = models.CharField(max_length=200, default='pelanggan')

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
