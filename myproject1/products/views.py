
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from . models import Product

# Create your views here.
def products(request):
    return render(request , 'products/products.html', {"pro":Product.objects.all()})


def product(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("product not found.")
    return render(request, 'products/product.html', {
        "product": product,
        #"passengers": flight.passengers.all(),
        #"non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

    #return render(request , 'products/product.html')
     


def search(request):
    return render(request , 'products/search.html')

