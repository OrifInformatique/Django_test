from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Register your models here.

from .models import Product, Reservation, ReservationRow

admin.site.register(Product)
# admin.site.register(Reservation)
# admin.site.register(ReservationRow)

class ReservationRowInline(admin.TabularInline):
    model = ReservationRow
    extra = 3

@admin.display(description=_("Reservation"))
def description(obj):
    return f"{obj}"

@admin.display(description=_("Invoice"))
def invoice_link(obj):
    # return f'<a href="/invoice/{obj.id}">lien</a>'
    return format_html(
        '<a href="{}" target="_blank">{}</a>',
        reverse('shop:invoice', args=[obj.id]),
        _('see')
    )

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
    list_display = [description, invoice_link]


admin.site.register(Reservation, ReservationAdmin)


