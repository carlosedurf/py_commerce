# Generated by Django 3.2.5 on 2021-07-20 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('A', 'Aprovado'), ('C', 'Criado'), ('R', 'Reprovado'), ('P', 'Pendente'), ('E', 'Enviado'), ('F', 'Finalizado')], default='C', max_length=1, verbose_name='Situação'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='image',
            field=models.CharField(max_length=2000, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Pedido'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.CharField(max_length=255, verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product_id',
            field=models.PositiveIntegerField(verbose_name='ID do Produto'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='promotional_price',
            field=models.FloatField(default=0, verbose_name='Preço Promocional'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='variation',
            field=models.CharField(max_length=255, verbose_name='Variação'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='variation_id',
            field=models.PositiveIntegerField(verbose_name='ID da Variação'),
        ),
    ]