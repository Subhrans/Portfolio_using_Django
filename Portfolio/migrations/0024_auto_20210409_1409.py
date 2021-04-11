# Generated by Django 3.0.1 on 2021-04-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0023_auto_20210408_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mydetail',
            old_name='alternative_text',
            new_name='profile_alternative_text',
        ),
        migrations.AddField(
            model_name='mydetail',
            name='optional_alternative_text',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='mailbackend',
            name='password',
            field=models.CharField(help_text="(Note): If You Dont't Have gmail App Password, Create that first else sending email is not being processed", max_length=200, verbose_name='App Password (gmail)'),
        ),
        migrations.AlterField(
            model_name='mydetail',
            name='optional_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Pics',
        ),
    ]