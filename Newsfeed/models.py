from django.db import models

# Create your models here.
class Country(models.Model):
    CName = models.CharField(max_length=100)
    CCode = models.CharField(max_length=2)
