from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0);
    image = models.ImageField(upload_to='shop\static\shop\images');
    
    def __str__(self):
        return f'{self.name} {self.description} {self.price}'





