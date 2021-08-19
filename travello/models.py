from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField(default=0)
    desc = models.TextField()
    offer = models.BooleanField(default=False)