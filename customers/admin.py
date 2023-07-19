from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'phone_number', 'get_address', 'loyalty_points')
    readonly_fields = ('loyalty_points',)

    def get_address(self, obj):
        # Implement the get_address method to return the customer's address
        address_parts = []
        if obj.door_no:
            address_parts.append(obj.door_no)
        if obj.street:
            address_parts.append(obj.street)
        if obj.city:
            address_parts.append(obj.city)
        if obj.pincode:
            address_parts.append(obj.pincode)
        if obj.state:
            address_parts.append(obj.state)
        if obj.country:
            address_parts.append(obj.country)

        return ", ".join(address_parts)

    get_address.short_description = 'Address'
