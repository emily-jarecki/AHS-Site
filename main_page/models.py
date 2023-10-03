from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80)
    products = models.ManyToManyField('Product', related_name='categories')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField()
    SKU = models.CharField()
    description = models.CharField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specialPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name()
    
    def price_of_product(self):
        return self.price()