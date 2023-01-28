# Generated by Django 4.1.3 on 2023-01-28 05:36

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_brand_slug_descriptions_slug_picture_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchased_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commercial_invoice', models.CharField(blank=True, max_length=100, null=True)),
                ('purchased_order', models.CharField(blank=True, max_length=100, null=True)),
                ('proforma_invoice', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=600, null=True)),
                ('part_number', models.CharField(blank=True, max_length=600, null=True)),
                ('quantity', models.SmallIntegerField(default=0)),
                ('category', models.CharField(blank=True, max_length=600, null=True)),
                ('initial_cost', models.DecimalField(decimal_places=2, default=1.0, max_digits=9)),
                ('cost_add_present', models.SmallIntegerField(default=0)),
                ('unit_cost', models.DecimalField(decimal_places=2, default=1.0, max_digits=9)),
                ('currency', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('barcode', models.ImageField(blank=True, upload_to='barcodes/')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('description', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.descriptions')),
            ],
        ),
        migrations.CreateModel(
            name='Ordered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(blank=True, default='admin_for_now', max_length=50, null=True)),
                ('Quantity', models.SmallIntegerField(default=1)),
                ('transaction_id', models.CharField(default=products.models.Ordered.getUniqueCode, max_length=20, verbose_name='transaction_id')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product_stock')),
            ],
        ),
    ]