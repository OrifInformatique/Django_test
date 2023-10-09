from django.contrib import admin

# Register your models here.

from .models import Product, Reservation, ReservationRow

admin.site.register(Product)
admin.site.register(Reservation)
admin.site.register(ReservationRow)
