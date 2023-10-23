from django.shortcuts import render
from .models import Product, ReservationRow, Reservation
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

def post_reservation_form(request):
    try:
        print(request.POST, type(request.POST), vars(request.POST),
              request.POST['datetime'])
        print(str(request.POST['datetime']))
        context = dict()
        reservation = Reservation.objects.create(date=request.POST['datetime'],
                           first_name=request.POST['first_name'],
                           last_name=request.POST['last_name'],
                           phone_number=request.POST['phone_number'])
        basket = request.session['basket']
        formated_basket = get_number_each_item(basket)
        print(formated_basket)
        for row in formated_basket:
            product = Product.objects.get(id=row['id'])
            ReservationRow.objects.create(number=row['number'], reduction=0,
                                  product=product, reservation=reservation)
        request.session['basket'] = list()
        return render(request, 'shop/summary.html', context)
    except Exception as e:
        print(e)

def get_number_item_in_list(item_list, compared_item): 
    print('begin get_number_item_in_list')
    def count_same_item(accumulator, item):
        print('begin count_same_item')
        if item == compared_item:
            accumulator += 1
        return accumulator
    return reduce(count_same_item, item_list, 0)
    

def get_number_each_item(basket):
    print('begin get_number_each_item')
    def get_number_and_id(item):
        print('begin get_number_and_id')
        print(basket)
        row = dict()
        row['number'] = get_number_item_in_list(basket, item)
        row['id'] = item
        return row
    count_basket = list(map(get_number_and_id, basket))
    def remove_duplicate(accumulator, item):
        print('begin remove_duplicate')
        if get_number_item_in_list(accumulator, item) > 1:
            accumulator.remove(item)
        return accumulator
    duplicateless_count_basket = reduce(remove_duplicate, count_basket,
                                        count_basket)
    return duplicateless_count_basket

def get_invoice(request, id):
    context = dict()
    reservation = Reservation.objects.get(id=id)
    products = list(map(set_url_image,
            reservation.products.all()))
    reservation_rows = reservation.reservationrow_set.all()
    def merge(t):
        reservation_row, product = t
        row = dict()
        row['Image'] = product.image
        row['name'] = product.name
        row['description'] = product.description
        row['number'] = reservation_row.number
        unit_price = product.price
        row['price'] = row['number'] * unit_price
        return row
    merged_reservation_rows = list(map(merge, zip(reservation_rows, products)))
    context['reservation_rows'] = merged_reservation_rows
    context['reservation'] = reservation
    return render(request, 'shop/invoice.html', context)
