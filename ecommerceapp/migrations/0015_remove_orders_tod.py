# Generated by Django 3.1.14 on 2023-02-09 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0014_auto_20230209_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='tod',
        ),
    ]