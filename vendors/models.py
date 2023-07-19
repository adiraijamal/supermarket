from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name= ('Vendor Name'))
    email = models.CharField(max_length=25, verbose_name= ('Email'))
    phone_number = models.CharField(max_length=10, unique=True, verbose_name= ('Phone Number'))
    address = models.CharField(max_length=25, verbose_name= ('Address'))

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phone_number}, Address: {self.address}"
