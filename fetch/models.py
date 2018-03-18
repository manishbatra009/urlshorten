from django.db import models

class urls(models.Model):
    longURL = models.TextField(blank=False)
    shortURL = models.CharField(max_length=8)
    count = models.IntegerField()

    def __str__(self):
        return "urls: ".format(self.shortURL)
    
# Create your models here.
