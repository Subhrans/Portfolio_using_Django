# Generated by Django 3.0.1 on 2021-03-26 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0005_auto_20210326_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
    ]