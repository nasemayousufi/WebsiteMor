from django.db import models
 


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()  # Quantity in stock
    size = models.CharField(max_length=20, blank=True, null=True)  # Optional, e.g., Small, Medium, Large
    color = models.CharField(max_length=50, blank=True, null=True)  # Optional, e.g., Red, Blue, Black
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)  # Image of the item

   
   

# Customer model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default="000-000-0000")
    email = models.EmailField(max_length=100, null=True, blank=True)

    

# Order model
class Order(models.Model):
    STATUS_PENDING = 'Pending'
    STATUS_SHIPPED = 'Shipped'
    STATUS_DELIVERED = 'Delivered'
    STATUS_CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_SHIPPED, 'Shipped'),
        (STATUS_DELIVERED, 'Delivered'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )
   

    


# ShippingAddress model
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    
   


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

    def get_total_price(self):
        return self.item.price * self.quantity



    
    

   