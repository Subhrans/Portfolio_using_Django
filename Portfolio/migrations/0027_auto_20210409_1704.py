# Generated by Django 3.0.1 on 2021-04-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0026_auto_20210409_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='', editable=False),
        ),
    ]
