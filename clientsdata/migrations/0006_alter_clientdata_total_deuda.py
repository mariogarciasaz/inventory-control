# Generated by Django 4.2.5 on 2023-09-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientsdata', '0005_clientdata_to_pay_alter_clientdata_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdata',
            name='total_deuda',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='Total Deuda'),
        ),
    ]
