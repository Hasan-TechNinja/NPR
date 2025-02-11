# Generated by Django 5.1.4 on 2025-01-04 21:45

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='Profile/', validators=[main.models.validate_size]),
        ),
    ]
