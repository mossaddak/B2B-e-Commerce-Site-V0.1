# Generated by Django 4.2.1 on 2023-06-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_shop_connection_shop_request_sender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='connection',
            field=models.ManyToManyField(blank=True, null=True, to='shop.shop'),
        ),
    ]