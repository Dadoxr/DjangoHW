# Generated by Django 4.2.5 on 2023-11-04 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 7, 52, 8, 737624, tzinfo=datetime.timezone.utc), verbose_name='дата создания'),
        ),
    ]
