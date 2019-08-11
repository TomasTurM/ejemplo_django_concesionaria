# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.


class TransaccionesAuto(admin.TabularInline):
    model = Transaccion


class AdminConcesionaria(admin.ModelAdmin):
    def cant_transacciones(self, obj):
        if obj:
            return obj.cant_transactions.count()

    list_display = ('car_model', 'car_brand', 'year')
    search_fields = ('car_model',)
    list_filter = ('car_brand', 'year')
    readonly_fields = ('cant_transacciones',)

    inlines = [
        TransaccionesAuto,
    ]


class AdminFinanzas(admin.ModelAdmin):
    list_display = ('car', 'transaction', 'price', 'date')
    search_fields = ('car__car_model', 'car__car_brand')
    list_filter = ('transaction', 'date')


admin.site.register(
    Auto, AdminConcesionaria
)

admin.site.register(
    Transaccion, AdminFinanzas
)