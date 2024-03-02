from django.db import models

class TodolistModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.BooleanField(default=False )

# Create your models here.
