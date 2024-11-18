from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django import forms
from .models import Product,Category

def about(request):
    
    return render(request, "about.html",{})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("you have been logged in"))
            return redirect('home')
        else:
            messages.error(request, ("Please enter valid crendentials"))
            return redirect('login_user')
    else:
        return render(request, "login.html",{})

def logout_user(request):
    logout(request)
    messages.success(request, ("you have been logged out"))
    return redirect('home')

def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create the user instance but don't save to the database yet
            password = form.cleaned_data['password']
            user.set_password(password)  # Hash the password before saving the user
            user.save()  # Now save the user with the hashed password

            # Authenticate the user
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, f"You have registered successfully, Welcome!")
                return redirect('home')  # Redirect to the home page or any other page
            else:
                messages.error(request, "Authentication failed. Please try logging in.")
                return redirect('login')

        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, "register.html", {'form': form})
            
    return render(request, "register.html", {'form': form})


def getProduct(request,pk):
    productData = Product.objects.get(id=pk)
    return render(request, "product.html",{"productData":productData})

def getCategoryProduct(request,pk):
    getcategoryData = Category.objects.get(id=pk)    
    productData = Product.objects.filter(category=getcategoryData)
    return render(request, "home.html",{"productData":productData})