# Generated by Django 4.1.3 on 2023-01-30 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_product_stock_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_stock',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.store'),
        ),
    ]
