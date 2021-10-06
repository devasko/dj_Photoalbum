from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False,verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'


class Picture(models.Model):
    description = models.TextField(max_length=500, null=False, blank=False, verbose_name='Описание')
    image = models.ImageField(null=False, blank=False, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
