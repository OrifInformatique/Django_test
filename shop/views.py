from django.shortcuts import render
from .models import Product

def index(request):
    context = dict()
    context['products'] = Product.objects.all().values()
    def add(product):
        product['image'] =  product['image'][11:] 
        #product['image'] = 'shop/images/' + product['image']
        return product
    context['products'] = list(map(add, context['products']))
    return render(request, 'shop/index.html', context)

def images(request, name):
    context = dict()
    context['src'] = 'shop/images/' + name
    return render(request, 'shop/images.html', context)
