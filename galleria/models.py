from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Location(models.Model):
    loc = models.CharField(max_length=50)

    def __str__(self):
        return self.loc
        
class Pictures(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    location = models.ForeignKey('Location',on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)



    @classmethod
    def search_by_category(cls,search_term):
        galleria = cls.objects.filter(category__name__icontains=search_term)
        return galleria
    
    @classmethod
    def get_all_pictures(cls):
        pictures = Pictures.objects.all()
        return pictures

    def save_picture(self):
        self.save()
    def delete_picture(self):
        my_obj = Pictures.objects.get(pk = id(1))
        self.delete(my_obj)
    def update_picture(self,name,description,category):
        self.name = name,
        self.description = description,
        self.category = category
        self.save()
    class Meta:
        ordering = ['name']


