from django.db import models


# Create your models here.
class URLShortner(models.Model):
    short_url = models.CharField(max_length=50, primary_key=True)
    long_url = models.CharField(max_length=2048)
    hits = models.IntegerField()
