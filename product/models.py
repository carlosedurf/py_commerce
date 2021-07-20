import product
from PIL import Image
from django.db import models
from django.conf import settings
from django.utils.text import slugify
import os


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    short_description = models.TextField(
        max_length=255,
        verbose_name='Descrição Curta'
    )
    long_description = models.TextField(verbose_name='Descrição Longa')
    image = models.ImageField(
        upload_to='product_image/%Y/%m/',
        blank=True,
        null=True,
        verbose_name='Imagem'
    )
    slug = models.CharField(
        unique=True,
        max_length=255,
        verbose_name='Sigla',
        blank=True,
        null=True
    )
    marketing_price = models.FloatField(verbose_name='Preço')
    promotional_marketing_price = models.FloatField(
        default=0,
        verbose_name='Preço Promocional'
    )
    type = models.CharField(
        default='V',
        max_length=1,
        verbose_name='Tipo',
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )

    def get_price_formated(self):
        return f'R$ {self.marketing_price:.2f}'.replace('.', ',')
    get_price_formated.short_description = 'Preço'

    def get_price_promotional_formated(self):
        return f'R$ {self.promotional_marketing_price:.2f}'.replace('.', ',')
    get_price_promotional_formated.short_description = 'Preço Promocional'

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)

        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Variation(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Produto'
    )
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Nome'
    )
    price = models.FloatField(verbose_name='Preço')
    promotion_price = models.FloatField(
        default=0,
        verbose_name='Preço Promocional'
    )
    stock = models.PositiveIntegerField(default=1, verbose_name='Estoque')

    def __str__(self):
        return self.name or self.product.name

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
