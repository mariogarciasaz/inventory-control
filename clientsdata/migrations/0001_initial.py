# Generated by Django 4.2.5 on 2023-09-08 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_enviada', models.IntegerField(verbose_name='Cantidad Enviada')),
                ('cantidad_vendida', models.IntegerField(blank=True, null=True, verbose_name='Cantidad Vendida')),
                ('cantidad_retirada', models.IntegerField(blank=True, null=True, verbose_name='Cantidad Retirada')),
                ('total_deuda', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Total Deuda')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client_data', to='clients.client', verbose_name='Client')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'ClientData',
                'verbose_name_plural': 'ClientDatas',
                'db_table': 'clientsdata',
                'ordering': ['-id'],
            },
        ),
    ]
