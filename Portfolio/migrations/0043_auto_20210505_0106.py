# Generated by Django 3.0.1 on 2021-05-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0042_auto_20210505_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='color',
            field=models.CharField(blank=True, default='#e91e63', help_text='Please enter only color codes or name, do not include rgba values', max_length=20, null=True, verbose_name='background color'),
        ),
    ]
