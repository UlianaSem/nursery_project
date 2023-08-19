from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Breed(models.Model):
    breed_name = models.CharField(max_length=100, verbose_name='название породы')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f"{self.breed_name}"

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'


class Dog(models.Model):
    dog_name = models.CharField(max_length=250, verbose_name='имя')
    breed_id = models.ForeignKey(Breed, models.SET_NULL, **NULLABLE)
    dog_photo = models.ImageField(upload_to='dogs/', verbose_name='фото', **NULLABLE)
    birthday = models.DateField(verbose_name='дата рождения', **NULLABLE)

    def __str__(self):
        return f"{self.dog_name} {self.birthday}"

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'