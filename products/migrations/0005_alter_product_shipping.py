# Generated by Django 4.1.1 on 2022-09-29 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_descriptions_measurement_product_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shipping',
            field=models.CharField(blank=True, choices=[(None, '--Please choose--'), ('Free', 'Free'), ('Not Free', 'Not Free'), ('on Stor pickup', 'on Stor pickup'), ('Buy 5+ get free', 'Buy 5+ get free'), ('let you know on checkout', 'let you know on checkout')], max_length=30, null=True),
        ),
    ]