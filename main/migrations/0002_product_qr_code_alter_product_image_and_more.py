# Generated by Django 5.1.4 on 2025-01-02 20:05

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='QR code/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='Product/', validators=[main.models.validate_size]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='Profile/', validators=[main.models.validate_size]),
        ),
    ]