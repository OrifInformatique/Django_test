from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('static/shop/images/<str:name>', views.images, name='images'),
    path('add-basket/<int:id>', views.add_basket, name='add-basket'),
    path('show-basket/', views.show_basket, name='show-basket'),
    path('delete-basket/', views.delete_basket, name='delete-basket'),
    path('delete-item-basket/<int:id>', views.delete_item_basket, name='delete-item-basket'),
]
