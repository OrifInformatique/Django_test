from django.db import models
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    description = models.CharField(max_length=255,
                                   verbose_name=_('Description'))
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                verbose_name=_('Price'))
    image = models.ImageField(upload_to='shop\static\shop\images',
                              verbose_name=_('Image'))
    
    def __str__(self):
        return f'{self.name} {self.description} {self.price}'

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Reservation(models.Model):
    date = models.DateTimeField(verbose_name=_('Date'))
    first_name = models.CharField(max_length=255, verbose_name=_('First name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last name'))
    phone_number = models.CharField(max_length=255,
                                    verbose_name=_('Phone number'))
    products = models.ManyToManyField(Product, through='ReservationRow',
                                      verbose_name=_('Products'))

    def __str__(self):
        return (f'[{naturaltime(self.date)}] {self.first_name} '
                f'{self.last_name.upper()} '
                f'({len(self.products.all())})')

    class Meta:
        verbose_name = _('Reservation')
        verbose_name_plural = _('Reservations')


class ReservationRow(models.Model):
    quantity = models.IntegerField(verbose_name=_('Quantity'))
    reduction = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                    verbose_name=_('Reduction'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name=_('Product'))
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE,
                                    verbose_name=_('Reservation'))

    def __str__(self):
        return f'quantity: {self.quantity} reduction: {self.reduction}'

    class Meta:
        verbose_name = _('Reservation row')
        verbose_name_plural = _('Reservation rows')

