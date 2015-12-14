from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    parent = models.ForeignKey('Category')
    pass

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    category = models.ForeignKey('Category')
    description = models.TextField() 
    photo = models.ImageField()
    pass

# Create your models here.
