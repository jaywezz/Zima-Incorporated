from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import ProductAddForm
from django.contrib import messages

# Create your views here.

def Home(reqeust):
    return HttpResponse("Home")

def AddProduct(request):
    if request.method == "POST":
        form = ProductAddForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            messages.success(request, "Added succesfully.")
            return redirect("products:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = ProductAddForm()
    return render(request=request, template_name="addproduct.html", context={"form": form})

