# Generated by Django 4.1.1 on 2022-10-09 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_is_buyer_customuser_is_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_buyer',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_seller',
        ),
    ]
