from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from functools import reduce
from django.shortcuts import redirect
from .forms import ResevationForm
import sys

def set_url_image(product):
    try:
        product['image'] =  product['image'][11:] 
    except TypeError as e:
        print(e, file=sys.stderr)
        product.image =  product.image.name[11:] 
    return product

def index(request):
    basket = request.session['basket']
    context = dict()
    context['products'] = Product.objects.all().values()
    context['products'] = list(map(set_url_image, context['products']))
    context['itemNumberBasket'] = len(basket)
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
        return redirect('shop:index')
    except (KeyError, AttributeError) as e:
        print(e, file=sys.stderr)
        request.session['basket'] = list()
        return add_basket(request, id)


def get_data_for_show_basket(id):
    try:
        return Product.objects.get(id=id)
    except Exception as e:
        print(e, file=sys.stderr)

def get_basket_with_url(basket):
    basket_data = tuple(map(get_data_for_show_basket, basket))
    basket_data_noneless = tuple(filter(lambda product: product is not None,
                                       basket_data))
    basket_with_url = tuple(map(set_url_image, basket_data_noneless))
    return basket_with_url

def get_total_price(basket):
    def sum_price(accumulator, product):
        return accumulator + product.price
    total_price = reduce(sum_price, basket, 0)
    return total_price

def get_basket_from_session(request):
    try:
        basket = request.session['basket']
    except (KeyError, AttributeError) as e:
        print(e, file=sys.stderr)
        request.session['basket'] = list()
        basket = request.session['basket']
    return basket

def show_basket(request):
    basket = get_basket_from_session(request)
    basket_with_url = get_basket_with_url(basket)
    context = dict()
    context['basket'] = basket_with_url
    context['total_price'] = get_total_price(basket_with_url)
    return render(request, 'shop/basket.html', context)
    
def delete_basket(request):
    request.session['basket'] = list()
    return redirect('shop:show-basket')

def delete_item_basket(request, id):
    try:
        basket = request.session['basket']
        basket.remove(id)
        request.session['basket'] = basket
    except ValueError as e:
        print(e, file=sys.stderr)
    return redirect('shop:show-basket')

def reservation_form(request):
    context = dict()
    context['form'] = ResevationForm();
    return render(request, 'shop/reservation-form.html', context)
