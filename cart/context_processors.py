# context_processors.py
from django.db import models
from .models import CartItem
from store.models import Category

# views.py
def cart_item_count(request):
    count=0
    if request.user.is_authenticated:
        count = CartItem.objects.filter(user=request.user).aggregate(total_quantity=models.Sum('quantity'))['total_quantity'] or 0

    else:
        count = sum(item['quantity'] for item in request.session.get('cart', {}).values())
    categoryData = Category.objects.all()
    return {'cart_item_count': count,"categoryData":categoryData}

