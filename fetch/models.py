from django.db import models

class URLS(models.Model):
    id = models.AutoField(primary_key=True)
    longURL = models.CharField(max_length=500)
    shortURL = models.CharField(max_length=8)
    count = models.IntegerField()

    def __str__(self):
        return "urls: ".format(self.shortURL)

# Create your models here.
