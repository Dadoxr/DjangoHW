# Generated by Django 4.2.5 on 2023-10-10 21:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_contact_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 21, 13, 3, 102502, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_change_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 21, 13, 3, 103073, tzinfo=datetime.timezone.utc), verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]