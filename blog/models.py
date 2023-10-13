from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(unique=True, max_length=170, verbose_name='ЧПУРЛ')
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(verbose_name='превью', null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.now(), verbose_name='дата создания')
    is_active = models.BooleanField(default=True, verbose_name='признак публикации')
    views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
