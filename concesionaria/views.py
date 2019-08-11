# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from concesionaria.models import Auto, Transaccion

# Create your views here.

def autos_render(request):
    context = {}
    context['autos'] = Auto.objects.all()
    return render(request, 'index.html', context)

#def car_render(request, id_car):
#    car_info = {}
#    id_car_int = int(id_car)
#    car_info['car'] = Auto.objects.get(id=id_car_int)
#    print car_info
#    return render(request, 'car.html', car_info)

def car_render(request, car_id):
    context = {}
    context['car'] = Auto.objects.get(id=car_id)
    return render(request, 'car.html', context)

def car_form(request):
    context = {}
    context['brands'] = Auto.BRANDS
    context['states'] = Auto.STATES
    return render(request, 'car_form.html', context)

def guardar_auto(request):
    if request.POST:
        model = request.POST.get('model', None)
        brand = request.POST.get('brand', None)
        state = request.POST.get('state', None)
        year = request.POST.get('year', None)
        payed_price = request.POST.get('payed_price', None)
        adq_date = request.POST.get('adq_date', None)
        buy_price = request.POST.get('buy_price', None)
        if model:
            newCar = Auto()
            newCar.car_model = model
            newCar.car_brand = brand
            newCar.car_state = state
            newCar.year = year
            newCar.save()

            transBuy = Transaccion()
            transBuy.car = newCar
            transBuy.date = adq_date
            transBuy.price = payed_price
            transBuy.save()

            transSell = Transaccion()
            transSell.car = newCar
            transSell.price = buy_price
        return redirect('/')