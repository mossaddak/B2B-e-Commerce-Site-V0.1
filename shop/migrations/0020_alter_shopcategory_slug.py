# Generated by Django 4.2.1 on 2023-06-05 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_shopcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
