from django.db import models


# Create your models here.

class New(models.Model):
    date = models.DateField()
    text_ja = models.TextField(max_length=200, blank=True)
    text_en = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to="./images", blank=True)