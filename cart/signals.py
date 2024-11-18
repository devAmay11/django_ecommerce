# signals.py
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import CartItem
from store.models import Product

@receiver(user_logged_in)
def merge_cart_on_login(sender, request, user, **kwargs):
    session_cart = request.session.get('cart', {})

    for product_id, item_data in session_cart.items():
        product = Product.objects.get(id=product_id)
        
        # Merge session cart with database cart
        cart_item, created = CartItem.objects.get_or_create(
            user=user,
            product=product,
            defaults={'quantity': item_data['quantity']}
        )
        if not created:
            cart_item.quantity += item_data['quantity']
            cart_item.save()

    # Clear session cart after merging
    request.session['cart'] = {}
    request.session.modified = True

