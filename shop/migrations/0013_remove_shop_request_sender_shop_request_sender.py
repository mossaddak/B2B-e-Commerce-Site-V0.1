# Generated by Django 4.2.1 on 2023-06-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_shop_connection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='request_sender',
        ),
        migrations.AddField(
            model_name='shop',
            name='request_sender',
            field=models.ManyToManyField(blank=True, null=True, to='shop.shop'),
        ),
    ]
