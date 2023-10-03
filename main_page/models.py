from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80)
    products = models.ManyToManyField('Product', related_name='categories')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=80)
    SKU = models.CharField(max_length=80)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=80)
    price = models.IntegerField()
    specialPrice = models.IntegerField()
    images = models.CharField(max_length=80)

    def __str__(self):
        return self.name()
    
    def price_of_product(self):
        return self.price()