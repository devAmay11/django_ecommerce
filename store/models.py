from django.db import models
import datetime
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    address = models.CharField(max_length=100,default="",blank=True)
    phone = models.CharField(max_length=20,default="",blank=True)
    status = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product
