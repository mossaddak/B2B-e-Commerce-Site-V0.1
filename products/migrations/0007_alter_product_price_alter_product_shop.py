# Generated by Django 4.2.1 on 2023-06-11 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0040_alter_connection_reciver_alter_connection_sender_and_more'),
        ('products', '0006_alter_product_price_alter_product_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='products', to='shop.shop'),
        ),
    ]