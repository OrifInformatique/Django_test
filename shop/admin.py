from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Register your models here.

from .models import Product, Reservation, ReservationRow


class ReservationRowInline(admin.TabularInline):
    model = ReservationRow
    extra = 3


@admin.display(description=_("Invoice"))
def invoice_link(obj):
    return format_html(
        '<a href="{}" target="_blank">{}</a>',
        reverse('shop:invoice', args=[obj.id]),
        _('see')
    )

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    inlines = [ReservationRowInline]
    fieldsets = [
          (
              None,
              {
                  "fields": ['date', 'first_name', 'last_name',
                             'phone_number'],
                  "description":
                  '<a href="http://127.0.0.1:8000/invoice/16">f</a>' 
              },
          ),
      ]
    list_display = ('date', 'first_name', 'last_name', 'phone_number',
                    invoice_link)
    list_filter = ['date']
    search_fields = ['first_name', 'last_name', 'phone_number',
                     'products__name']
    list_per_page = 100

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ['name', 'description']
    list_per_page = 100
