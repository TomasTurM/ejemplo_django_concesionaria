# Generated by Django 2.0.6 on 2018-06-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concesionaria', '0002_auto_20180622_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='transaction',
            field=models.CharField(choices=[('Reparacion', 'REPARACION'), ('Compra', 'COMPRA'), ('Venta', 'VENTA')], max_length=20, verbose_name='Tipo de Transaccion'),
        ),
    ]
