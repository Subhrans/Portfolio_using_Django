# Generated by Django 3.0.1 on 2021-04-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0010_auto_20210406_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social_site_connection',
            name='facebook',
            field=models.URLField(default=''),
        ),
    ]
