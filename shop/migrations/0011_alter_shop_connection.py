# Generated by Django 4.2.1 on 2023-06-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_shop_connection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='connection',
            field=models.ManyToManyField(blank=True, limit_choices_to=models.Q(('pk', models.F('_id')), _negated=True), null=True, to='shop.shop'),
        ),
    ]
