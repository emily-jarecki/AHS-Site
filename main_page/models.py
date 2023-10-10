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
        return self.name
    
class Quote(models.Model):
    cookie = models.CharField()
    email =  models.EmailField(max_length=254)
    item = models.CharField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.cookie