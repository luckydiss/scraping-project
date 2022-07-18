from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Название населенного пункта')
    plug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Название населенных пунктов'

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Язык программирования')
    plug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name