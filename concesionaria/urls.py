from django.urls import path, include
from . import views

app_name="concesionaria"

urlpatterns = [
    path('', views.autos_render, name='autos_render'),
    #path('car/<int:car_id>', views.car_render, name='car_render_url'),
    path('car_render_url/<int:car_id>', views.car_render, name="car_render_url"),
    path('car_form', views.car_form, name='car_form_url'),
    path('guardar_auto', views.guardar_auto, name='save_car_url'),
    path('api-auth/', include('rest_framework.urls')),
]
