# Generated by Django 4.2.1 on 2023-06-07 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
