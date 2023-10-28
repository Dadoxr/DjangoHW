from django.db import models
from django.utils import timezone 

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Наименование', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)

class Product(models.Model): 
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', **NULLABLE)
    price = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(default=timezone.now(), verbose_name='Дата создания')
    last_change_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}({self.category}): {self.description}\
            \nЦена:{self.price}\
            \nДата создания: {self.created_at}\
            \nДата последнего изменения: {self.last_change_date}\n'
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('id',)


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', null=True, blank=True)
    phone = models.BigIntegerField(verbose_name='Телефон', null=True, blank=True)
    message = models.TextField(verbose_name='Сообщение', null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.phone}\nСообщение: {self.message}'
    
    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('id',)

class Version(models.Model):
    CHOICES = (
        (1, "1 - Старт"),
        (2, "2- Базовый"),
        (3, "3 - Начал нормально работать"),
        (4, "4 - Я устал работать"),
        (5, "5 - Все, больше не сделаю"),
)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='id продукта')
    version = models.IntegerField(choices=CHOICES, verbose_name='версия')
    name = models.CharField(max_length=150, verbose_name='название')
    is_active = models.BooleanField(default=True, verbose_name='активен')

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'