# Generated by Django 3.0.1 on 2021-04-06 19:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Portfolio', '0015_contactbackend_gmail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactBackend',
            new_name='MailBackend',
        ),
    ]
