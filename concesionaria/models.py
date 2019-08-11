# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Auto(models.Model):
    car_model = models.CharField(max_length=20, verbose_name='Modelo')

    BRANDS = {
        ('Ford', 'FORD'),
        ('Chevrolet', 'CHEVROLET'),
    }

    car_brand = models.CharField(max_length=20, choices=BRANDS, verbose_name='Marca')

    year = models.CharField(max_length=4, verbose_name='Año')

    STATES = {
        ('Nuevo', 'NUEVO'),
        ('Usado', 'USADO'),
    }

    car_state = models.CharField(null=True, max_length=10, choices=STATES, verbose_name='Estado')

    #year_abr = year[-2:]

    def __str__(self):
        return "{} {} '{} - {}".format(self.car_brand, self.car_model, self.year_abr, self.car_state)

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'


class Transaccion(models.Model):
    car = models.ForeignKey('Auto', on_delete=models.CASCADE, verbose_name='Auto', related_name='cant_transactions')

    date = models.DateField(auto_now=False, null=True, blank=False, verbose_name='Fecha')

    price = models.IntegerField(null=True, blank=False, verbose_name='Precio')

    TRANSACTION = {
        ('Compra', 'COMPRA'),
        ('Venta', 'VENTA'),
        ('Reparacion', 'REPARACION')
    }

    transaction = models.CharField(max_length=20, choices=TRANSACTION, verbose_name='Tipo de Transaccion')

    def __str__(self):
        return '{} {}'.format(self.transaction, self.car)

    class Meta:
        verbose_name = 'Transaccion'
        verbose_name_plural = 'Transacciones'