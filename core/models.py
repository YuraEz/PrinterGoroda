from django.db import models


class OrderedCall(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Заказной звокнок'
        verbose_name_plural = 'Заказые звонки'

    def __str__(self):
        return f'Заказ {self.id}'

