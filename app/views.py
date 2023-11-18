from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Product

def index(request):
    product = Product.objects.all()
    return render(request, "product_index.html", {"product": product})


def create_product(request):
    if request.POST:
        name = request.POST.get("name")
        product = Product(name=name)
        product.save()
        return redirect("client_index")