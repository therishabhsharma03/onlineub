# Generated by Django 3.1.14 on 2023-02-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0012_auto_20230205_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='tod',
            field=models.TimeField(),
        ),
    ]