# Generated by Django 5.2 on 2025-05-05 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_review_helpful_review_not_helpful'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], max_length=1),
        ),
    ]
