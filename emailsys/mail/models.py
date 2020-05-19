from django.db import models
from django.conf import settings
# Create your models here.

class emails(models.Model):
    mail = models.EmailField()

class mess(models.Model):
    message = models.TextField()
    subject = models.TextField()
    