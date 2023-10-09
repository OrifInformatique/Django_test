from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0);
    image = models.ImageField(upload_to='shop\static\shop\images');
    
    def __str__(self):
        return f'{self.name} {self.description} {self.price}'


class Reservation(models.Model):
    date = models.DateTimeField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through='ReservationRow')


class ReservationRow(models.Model):
    number = models.IntegerField()
    reduction = models.DecimalField(max_digits=12, decimal_places=2,
                                    default=0);
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)



