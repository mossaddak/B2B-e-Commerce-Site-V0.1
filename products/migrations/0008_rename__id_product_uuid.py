# Generated by Django 4.2.1 on 2023-06-11 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_price_alter_product_shop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='_id',
            new_name='uuid',
        ),
    ]