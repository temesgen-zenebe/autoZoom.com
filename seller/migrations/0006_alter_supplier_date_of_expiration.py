# Generated by Django 4.1.1 on 2022-10-08 23:57

from django.db import migrations, models
import seller.models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_supplier_confirmation_supplier_website_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='date_of_expiration',
            field=models.DateField(help_text='contract expiration date', validators=[seller.models.validate_future_date], verbose_name='contract expiration date'),
        ),
    ]