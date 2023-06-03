from django.http import JsonResponse
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from . models import Product
import json

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
        
    })

    #return render(request , 'products/product.html')
     


def search(request):
    return render(request , 'products/search.html')



def basket_add(request):
    basket = []
    if request.method == 'POST':
        productid = request.POST.get('productid')
        productqty = request.POST.get('productqty')

        # Retrieve the basket from the session or browser local storage
       

        # Retrieve the product from the database
        product = Product.objects.get(id=productid)

        # Add the product to the basket
        basket.append({
            'id': product.id,
            'name': product.pname,
            'price': product.price,
            'quantity': int(productqty)
        })

        basket = json.loads(request.POST.get('basket'))
        print('Basket contents:', basket)

        # Store the updated basket in the session or browser local storage
        
        data = {'success': True}
        return JsonResponse(data)
    else:
        data = {'success': False}
        return JsonResponse(data)



def basket_view(request):
    basket = request.session.get('basket', [])
    
    # Convert the basket list to a list of products
    products = []
    for item in basket:
        product = Product.objects.get(id=item['id'])
        products.append({
            'name': product.pname,
            'price': product.price,
            'quantity': item['qty']
        })

    context = {
        'basket': products
    }
    return render(request, 'products/basket.html', context)



