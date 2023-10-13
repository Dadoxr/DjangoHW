# Generated by Django 4.2.5 on 2023-10-12 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_contact_phone_alter_product_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 14, 59, 3, 801511, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_change_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 14, 59, 3, 801994, tzinfo=datetime.timezone.utc), verbose_name='Дата последнего изменения'),
        ),
    ]
