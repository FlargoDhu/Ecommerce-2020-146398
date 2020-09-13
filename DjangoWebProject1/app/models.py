"""
Definition of models.
"""
from django.db.models import JSONField
from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=200)
    how_many_in_storage = models.IntegerField()
    price_grosze = models.IntegerField()

    def __str__(self): 
        return self.product_name 
# Create your models here.


class Orders(models.Model):
    req_title = models.CharField(max_length = 30)
    price_grosze = models.IntegerField()
    product_container = JSONField(null=True)
    product_ammounts = JSONField(null=True)
    product_prices = JSONField(null=True)
