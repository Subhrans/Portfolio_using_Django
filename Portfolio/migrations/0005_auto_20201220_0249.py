# Generated by Django 3.0.1 on 2020-12-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0004_auto_20201220_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievment',
            name='expiry_date',
            field=models.CharField(choices=[('1', 'none'), ('2', models.DateField())], max_length=200),
        ),
    ]
