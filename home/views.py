from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Item
from decimal import Decimal 
from django.contrib import messages


# Create your views here.
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'home/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
    
def about(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'home/about.html',
        {
            'title':'About',
            'year':datetime.now().year,
        }
    )
def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'home/item_detail.html', {'item': item})   

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items}) 


def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    item = get_object_or_404(Item, id=item_id)
    
    # Check if item is already in the cart; if so, increase the quantity
    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1
    else:
        # Add item with quantity 1, including image URL
        cart[str(item_id)] = {
            'name': item.name,
            'price': str(item.price),
            'quantity': 1,
            'image_url': item.image.url if item.image else None  # Include the image URL
        }

    request.session['cart'] = cart  # Save cart back to session
    return redirect('cart_view')  # Redirect to the cart page

# View to display cart page
def cart_view(request):
    cart = request.session.get('cart', {})
    total_price = Decimal(0)
    
    # Calculate item totals and total price
    for item in cart.values():
        item['item_total'] = Decimal(item['price']) * item['quantity']
        total_price += item['item_total']
    
    return render(request, 'home/cart.html', {'cart': cart, 'total_price': total_price})
# View to remove item from cart
def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    
    # Remove item if it's in the cart
    if str(item_id) in cart:
        del cart[str(item_id)]
        request.session['cart'] = cart  # Update cart in session
    
    return redirect('cart_view')

def contact(request):
    if request.method == 'POST':
        # Retrieve form data based on the fields in your form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Combine first_name and last_name if needed
        full_name = f"{first_name} {last_name}"

        # Here, you can add code to save the data to the database or send an email
        # For now, we'll just show a success message
        messages.success(request, 'Thank you for your message! We will get back to you soon.')

    return render(request, 'home/contact.html')
