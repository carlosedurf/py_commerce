import product
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, FloatField, PositiveIntegerField


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = FloatField()
    status = CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Pedido N. {self.pk}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price = FloatField()
    promotional_price = FloatField(default=0)
    quantity = PositiveIntegerField()
    image = CharField(max_length=2000)

    def __str__(self):
        return f'Item do {self.order}'

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do Pedido'
