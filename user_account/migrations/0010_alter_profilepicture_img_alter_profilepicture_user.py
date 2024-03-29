# Generated by Django 4.2.1 on 2023-06-08 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0009_alter_profilepicture_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicture',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profilepicture',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_picture', to=settings.AUTH_USER_MODEL),
        ),
    ]
