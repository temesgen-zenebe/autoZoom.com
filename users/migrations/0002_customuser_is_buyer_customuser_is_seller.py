# Generated by Django 4.1.1 on 2022-10-08 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_buyer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_seller',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
