from django.db import models
from vendors.models import Vendor

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name= ('Product Name'))
    description = models.CharField(max_length=50, verbose_name= ('Description'))
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name= ('Cost Price'))
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name= ('Selling Price'))
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Vendor: {self.vendor}, Cost Price: {self.cost_price}, Selling Price: {self.selling_price},  Quantity: {self.quantity}"
