# Generated by Django 3.1.14 on 2022-12-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_auto_20221220_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='', upload_to='images/images'),
        ),
    ]
