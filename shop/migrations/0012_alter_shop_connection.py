# Generated by Django 4.2.1 on 2023-06-02 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_shop_connection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='connection',
            field=models.ManyToManyField(blank=True, null=True, to='shop.shop'),
        ),
    ]
