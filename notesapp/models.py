from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('note title', max_length=500)
    content = models.CharField('note content', max_length=10000)
    slug_title = models.SlugField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)