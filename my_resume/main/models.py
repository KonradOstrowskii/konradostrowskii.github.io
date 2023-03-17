# main/models.py

from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos')
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
