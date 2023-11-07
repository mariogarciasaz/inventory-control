from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Product Name')
    description = models.CharField(max_length=255, blank=False, null=False, verbose_name='Product Description')
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False, verbose_name='Price')
    quantity = models.IntegerField(max_length=10, blank=False, null=False, verbose_name='Quantity')


    def __str__(self):
        return self.name


