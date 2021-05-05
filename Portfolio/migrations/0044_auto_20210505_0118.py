# Generated by Django 3.0.1 on 2021-05-04 19:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Portfolio', '0043_auto_20210505_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(default='', help_text='Please Add less than 100 characters, else rest of the text automatically hide.', max_length=100, verbose_name='little Description'),
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together={('user', 'name')},
        ),
    ]
