from django.contrib import admin
from .models import Item
from .models import Customer
from .models import ShippingAddress
from .models import Order
from .models import CartItem


# Register your models here.

admin.site.register(Customer)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(CartItem)


