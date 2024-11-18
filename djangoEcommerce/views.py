from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product,Category

def home(request):
    productData = Product.objects.all()
    categoryData = Category.objects.all()
    return render(request, "home.html",{"productData":productData,"categoryData":categoryData})