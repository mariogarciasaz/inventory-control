from typing import Type
from django.db import models
from django.db.models.options import Options
from products.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.



class Client(models.Model):
    fullname = models.CharField(max_length=255, blank=False, null=False, verbose_name='Fullname')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name='Phone')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Address')

    def __str__(self):
        return self.fullname
    

    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['-id']
