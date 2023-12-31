# Generated by Django 4.2.5 on 2023-09-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientsdata', '0004_clientdata_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdata',
            name='to_pay',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='A pagar'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='paid',
            field=models.BooleanField(blank=True, default=False, verbose_name='Paid'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='total_deuda',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='Total Deuda'),
        ),
    ]
