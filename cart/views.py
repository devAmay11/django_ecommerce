from django.shortcuts import render
from store.models import Product
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect
from .models import CartItem, Product
from django.db import models

# views.py
def add_to_cart(request):
    product_id = request.POST['product_id']
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        # Handle cart for authenticated user
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': 1}
        )
        if not created:
            # If the item already exists in the cart, increase the quantity
            cart_item.quantity += 1
            cart_item.save()
        # Calculate the total cart item count for authenticated user
        cart_item_count = CartItem.objects.filter(user=request.user).aggregate(total_quantity=models.Sum('quantity'))['total_quantity'] or 0
    else:
        # Handle cart for unauthenticated user using session
        cart = request.session.get('cart', {})
        
        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] += 1
        else:
            cart[str(product_id)] = {
                'product_name': product.name,
                'quantity': 1,
                'price': product.price,
                'created_at':str(datetime.now)
            }

        request.session['cart'] = cart
        request.session.modified = True
        # Calculate the total cart item count for unauthenticated user
        cart_item_count = sum(item['quantity'] for item in cart.values())
    # Prepare the response data
    print("----------cart_item_count",cart_item_count)
    response_data = {
        'cart_item_count': cart_item_count  # Get the updated cart count
    }

    return JsonResponse(response_data)  # Return JSON response
    
def view_cart(request):
    product_ids = []
    if request.user.is_authenticated:
        print('---if-------')
        product_ids = CartItem.objects.filter(user=request.user).values_list('product_id', flat=True)
    else:
        # Handle cart for unauthenticated user using session
        cart = request.session.get('cart', {})
        if cart:
            print('---else-------',cart)
            product_ids = list(map(int, cart.keys()))
    print('---product_ids-------',product_ids)
    productData = Product.objects.filter(id__in=product_ids)
    return render(request, "cart_view.html",{"productData":productData})