# Generated by Django 4.2.5 on 2023-09-28 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_begin_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='begin_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 28, 12, 14, 35, 587473, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_change_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 28, 12, 14, 35, 587937, tzinfo=datetime.timezone.utc), verbose_name='Дата последнего изменения'),
        ),
    ]
