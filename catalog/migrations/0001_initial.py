# Generated by Django 4.2.5 on 2023-09-28 12:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('preview', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('price', models.FloatField(verbose_name='Цена за покупку')),
                ('begin_date', models.DateField(default=datetime.datetime(2023, 9, 28, 12, 11, 57, 291711), verbose_name='Дата создания')),
                ('last_change_date', models.DateField(default=datetime.datetime(2023, 9, 28, 12, 11, 57, 291742), verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'ordering': ('name',),
            },
        ),
    ]
