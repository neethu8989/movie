from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    dscrptn = models.TextField()
    year = models.TextField()
    img=models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
