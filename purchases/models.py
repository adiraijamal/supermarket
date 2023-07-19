from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from vendors.models import Vendor

class Purchase(models.Model):
    cashier = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendors', to_field='name')
    purchase_date = models.DateField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Cashier: {self.cashier.username}, Product: {self.product.name}, Vendor: {self.vendor.name}, Purchase Date: {self.purchase_date}, Cost Price: {self.cost_price}, Quantity: {self.quantity}"
