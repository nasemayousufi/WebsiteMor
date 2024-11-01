from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
     #path('', views.index, name='home'),
    path('items/', views.item_list, name='item_list'),  # URL for item list view
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),  # URL for item detail view
    path('cart/', views.cart_view, name='cart_view'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('contact/', views.contact, name='contact'),
    
]