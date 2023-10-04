from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def set_url_image(product):
    try:
        product['image'] =  product['image'][11:] 
    except TypeError as e:
        print(e)
        print(vars(product.image))
        product.image =  product.image.name[11:] 
    return product

def index(request):
    context = dict()
    context['products'] = Product.objects.all().values()
    context['products'] = list(map(set_url_image, context['products']))
    return render(request, 'shop/index.html', context)

def images(request, name):
    context = dict()
    context['src'] = 'shop/images/' + name
    return render(request, 'shop/images.html', context)

def add_basket(request, id):
    try:
        return_text = ''
        basket = request.session['basket']
        return_text += str(request.session['basket'])
        basket.append(id)
        return_text += str(request.session['basket'])
        request.session['basket'] = basket
        return HttpResponse(return_text)
    except (KeyError, AttributeError) as e:
        print(e)
        request.session['basket'] = list()
        return add_basket(request, id)


def show_basket(request):
    basket = request.session['basket']
    def get_data(id):
        return Product.objects.get(id=id)
    basket_data = map(get_data, basket)
    basket_with_url = map(set_url_image, basket_data)
    context = dict()
    context['basket'] = list(basket_with_url)
    
    return render(request, 'shop/basket.html', context)
    
def delete_basket(request):
    request.session['basket'] = list()
    return HttpResponse('')
