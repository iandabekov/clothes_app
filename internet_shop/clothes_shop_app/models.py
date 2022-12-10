from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория одежды')

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Clothes(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название одежды')
    description = models.TextField(max_length=500, verbose_name='Описание одежды')
    price = models.IntegerField(null=False, blank=False, verbose_name='Цена')
    sizes_available = models.CharField(max_length=50, null=False, blank=False, default='M')
    image = models.ImageField(upload_to='images', blank=True, verbose_name='Картинка одежды')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'одежду'
        verbose_name_plural = 'Одежды'

    def __str__(self):
        return f'{self.name}, {self.added_at}'
