# Generated by Django 4.1.1 on 2022-09-30 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]
