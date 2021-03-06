# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Computer(models.Model):
#	title = models.CharField(max_length=200)
	Price = models.TextField()
	Description= models.TextField()
	Brand = models.TextField()
	Path = models.TextField()
#	created_at = models.DateTimeField(auto_now_add=True)
def __str__(self):
	return "[{} , {} , {} , {}]".format(self.Price,self.Description,self.Brand,self.Path)

class Tablet(models.Model):
	Price = models.TextField()
        Description= models.TextField()
        Brand = models.TextField()
        Path = models.TextField()

class Smartphone(models.Model):
        Price = models.TextField()
        Description= models.TextField()
        Brand = models.TextField()
        Path = models.TextField()

class Products(models.Model):
	Price = models.TextField()
        Description= models.TextField()
        Brand = models.TextField()
        Path = models.TextField()
	Type = models.TextField()

class SalesDetails(models.Model):
#	user_id=models.ForeignKey(User,to_field="id",db_column="user_id")
#	product_id=models.ForeignKey(Products,to_field="id",db_column="product_id")
	user_id=models.TextField()
	product_id=models.TextField()
	class Meta:
		unique_together = (("user_id", "product_id"),)
