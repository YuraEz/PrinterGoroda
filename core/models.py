from django.db import models


class OrderedCall(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=17)

    class Meta:
        verbose_name = 'Заказной звокнок'
        verbose_name_plural = 'Заказые звонки'

    def __str__(self):
        return f'Заказ {self.id}'


class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    sessid = models.CharField(max_length=100)
    baseCost = models.DecimalField(max_digits=10, decimal_places=2)
    finalCost = models.DecimalField(max_digits=10, decimal_places=2)
    ballsType = models.CharField(max_length=10)
    balls = models.DecimalField(max_digits=10, decimal_places=2)
    promocode = models.ForeignKey('PromoCode', on_delete=models.SET_NULL, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    messenger = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class User(models.Model):
    phone = models.CharField(max_length=20)
    fio = models.CharField(max_length=100)
    balls = models.DecimalField(max_digits=10, decimal_places=2)


class PromoCode(models.Model):
    code = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    mode = models.CharField(max_length=20)


class PromoCodeUses(models.Model):
    code = models.ForeignKey('PromoCode', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
