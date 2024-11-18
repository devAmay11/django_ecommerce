from django.db import models
from store.models import Product
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=datetime.now, blank=True)