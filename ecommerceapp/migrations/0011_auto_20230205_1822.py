# Generated by Django 3.1.14 on 2023-02-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0010_orders_tod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='tod',
            field=models.TimeField(),
        ),
    ]
