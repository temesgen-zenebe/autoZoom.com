# Generated by Django 4.1.3 on 2023-01-29 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_purchased_product_cost_add_present'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_stock',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.purchased_product'),
        ),
    ]
