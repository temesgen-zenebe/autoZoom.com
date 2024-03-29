# Generated by Django 4.1.3 on 2023-01-29 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_purchased_product_ordered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost_distribution_rat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commercial_invoice', models.CharField(blank=True, max_length=100, null=True)),
                ('total_Product_cost', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('shipping_costs', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('customs_fees', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('risk_coverage', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('overhead_charges', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('service_fees', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('cost_add_present', models.SmallIntegerField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='purchased_product',
            name='cost_add_present',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.PROTECT, to='products.cost_distribution_rat'),
        ),
    ]
