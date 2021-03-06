 # -*- coding: utf-8 -*-
from django.db import models
from autoslug import AutoSlugField
from pytils.translit import slugify
from django.conf import settings
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

class SessionBasket(models.Model):
    session_key = models.TextField()
    creation_ts = models.DateField(auto_now_add = True)
    

class BasketProduct(models.Model):
    session = models.ForeignKey(SessionBasket)
    product = models.ForeignKey('Product')
    quantity= models.IntegerField(default=1)

class Order(models.Model):
    #user = models.ForeignKey(User)
    creation_ts = models.DateField(auto_now_add = True)
    uid   = models.TextField()
    status = models.TextField(choices=(('prepare','Подготовка'),('build','Сборка'),('delivering','Доставка'),('complete','Завершен')), default='prepare')
    name   = models.TextField()
    email   = models.TextField()
    address   = models.TextField()
    phone   = models.TextField()
    comment = models.TextField(null=True, blank=True)

class OrderProducts(models.Model):
    order = models.ForeignKey('Order')
    product = models.ForeignKey('Product')
    quantity= models.IntegerField(default=1)
    
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    parent = models.ForeignKey('Category', null=True, blank=True)
    photo = ImageField(null=True, blank=True)
    def save(self):
        self.slug  = slugify(self.title)
        if (self.parent): self.slug = self.parent.slug+'_'+self.slug
        counter = 0
        original_slug = self.slug
        while (Category.objects.exclude(id=self.id or 0).filter(slug=self.slug).count()>0):
            counter+=counter
            self.slug = original_slug+'_'+str(counter)

        super(Category,self).save()
    def __str__(self):
        result = ''
        if (self.parent):
            result+=self.parent.title
        result+=self.title
        return result

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    category = models.ForeignKey('Category')
    description = models.TextField() 
    photo = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    quantity = models.IntegerField(default = 0 )
    creation_ts = models.DateField(auto_now_add = True)
    def __str__(self):
        return self.title

class Slider(models.Model):
    photo = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.photo.url

# Create your models here.
