# Generated by Django 3.0.1 on 2021-03-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0004_auto_20210326_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mydetail',
            name='projects_detail',
        ),
        migrations.AddField(
            model_name='mydetail',
            name='projects_detail',
            field=models.ManyToManyField(related_name='projects', to='Portfolio.Project'),
        ),
    ]