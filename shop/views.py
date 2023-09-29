from django.shortcuts import render


def index(request):
    context = dict()
    return render(request, 'shop/index.html', context)

def images(request, name):
    context = dict()
    context['src'] = 'shop/images/'+ name
    return render(request, 'shop/images.html', context)
