# Generated by Django 4.2.5 on 2023-10-28 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 28, 15, 30, 24, 296096, tzinfo=datetime.timezone.utc), verbose_name='дата создания'),
        ),
    ]
