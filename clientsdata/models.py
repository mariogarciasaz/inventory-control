from django.db import models
from clients.models import Client
from products.models import Product

# Create your models here.





class ClientData(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_data', verbose_name='Client')
    product = models.ForeignKey(Product, blank=False, null=True, on_delete=models.SET_NULL,verbose_name='Producto')
    cantidad_enviada = models.IntegerField(blank=False, null=False, verbose_name='Cantidad Enviada')
    cantidad_vendida = models.IntegerField(blank=True, null=True, verbose_name='Cantidad Vendida')
    cantidad_retirada = models.IntegerField(blank=True, null=True, verbose_name='Cantidad Retirada')
    total_deuda = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=False, verbose_name='Total Deuda')
    paid = models.BooleanField(blank=True, null=False, default=False, verbose_name= 'Paid')
    start_date = models.DateField(blank=False, null=False, verbose_name= 'Start Date')
    

    def __str__(self):
        return f"{self.client.fullname} + ' ' + '-' + {self.total_deuda}"
    

    class Meta:
        db_table = 'clientsdata'
        verbose_name = 'ClientData'
        verbose_name_plural = 'ClientDatas'
        ordering = ['-id']