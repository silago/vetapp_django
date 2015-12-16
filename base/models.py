from django.db import models
from autoslug import AutoSlugField
from pytils.translit import slugify
from django.conf import settings
from sorl.thumbnail import ImageField

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    parent = models.ForeignKey('Category', null=True, blank=True)
    photo = ImageField(null=True, blank=True)
    def save(self):
        self.slug  = slugify(self.title)
        super(Category,self).save()
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    category = models.ForeignKey('Category')
    description = models.TextField() 
    photo = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    quantity = models.IntegerField(default = 0 )
    creation_ts = models.DateField(auto_now_add = True)

# Create your models here.
