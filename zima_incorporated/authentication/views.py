from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.contrib import messages
from django.contrib.auth import login
from . models import Account

# Create your views here.
from .forms import NewUserForm, LoginForm



def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            Login(request, user)
            return redirect('products:home')
        elif user is None:
            print("no user found")
    else:
        form = LoginForm
        return render(request, "login.html", {'form': form})


def Register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("products:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"form": form})
