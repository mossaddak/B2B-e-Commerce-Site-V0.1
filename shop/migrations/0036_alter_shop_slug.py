# Generated by Django 4.2.1 on 2023-06-09 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_alter_shop_slug_alter_shop_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
    ]
