from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('static/shop/images/<str:name>', views.images, name='images'),
]
