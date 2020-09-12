"""
Definition of models.
"""

from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=200)
    how_many_in_storage = models.IntegerField()

    def __str__(self): 
        return self.product_name 
# Create your models here.
