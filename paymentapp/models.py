from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

# Create your models here.
