# Generated by Django 3.1.14 on 2023-02-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0011_auto_20230205_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='tod',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
