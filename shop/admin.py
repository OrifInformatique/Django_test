from django.contrib import admin

# Register your models here.

from .models import Product, Reservation, ReservationRow

admin.site.register(Product)
# admin.site.register(Reservation)
# admin.site.register(ReservationRow)

class ReservationRowInline(admin.TabularInline):
    model = ReservationRow
    extra = 3

class ReservationAdmin(admin.ModelAdmin):
    inlines = [ReservationRowInline]

admin.site.register(Reservation, ReservationAdmin)


