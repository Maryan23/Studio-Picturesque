from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Pictures(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
#     location = models.ForeignKey(Location)
#     category = models.ForeignKey(Category)

#     def __str__(self):
#         return self.name

# class Location(models.Model):

