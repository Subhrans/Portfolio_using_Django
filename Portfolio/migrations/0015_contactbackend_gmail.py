# Generated by Django 3.0.1 on 2021-04-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0014_contactbackend'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactbackend',
            name='gmail',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
