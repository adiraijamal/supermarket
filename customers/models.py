from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    fname = models.CharField(max_length=25, verbose_name=_('First Name'))
    lname = models.CharField(max_length=25, verbose_name=_('Last Name'))
    phone_number = models.CharField(max_length=10, unique=True, verbose_name=_('Phone Number'))
    loyalty_points = models.IntegerField(default=0, verbose_name=_('Loyalty Points'))
    door_no = models.CharField(max_length=10, verbose_name=_('Door Number'))
    street = models.CharField(max_length=25, verbose_name=_('Street'))
    city = models.CharField(max_length=25, verbose_name=_('City'))
    state = models.CharField(max_length=25, verbose_name=_('State'))
    country = models.CharField(max_length=25, verbose_name=_('Country'))
    pincode = models.CharField(
        max_length=6,
        validators=[RegexValidator('^[0-9]{6}$', _('Invalid postal code'))],
        verbose_name=_('Pincode')
    )

    def get_address(self):
        address_parts = []
        if self.door_no:
            address_parts.append(self.door_no)
        if self.street:
            address_parts.append(self.street)
        if self.city:
            address_parts.append(self.city)
        if self.pincode:
            address_parts.append(self.pincode)
        if self.state:
            address_parts.append(self.state)
        if self.country:
            address_parts.append(self.country)

        return ", ".join(address_parts)

    def __str__(self):
        return (
            f"First Name: {self.fname}\n"
            f"Last Name: {self.lname}\n"
            f"Phone Number: {self.phone_number}\n"
            f"Address: {self.get_address()}"
        )
