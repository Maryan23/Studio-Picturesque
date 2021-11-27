from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Pictures(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)

    @classmethod
    def search_by_name(cls,search_term):
        galleria = cls.objects.filter(name__icontains=search_term)
        return galleria

