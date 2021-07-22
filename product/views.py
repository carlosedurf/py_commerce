from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse, request
from django.contrib import messages
from django.urls import reverse
from .models import Product, Variation

from pprint import pprint


class ListProduct(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 9


class ProductDetails(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class AddCar(View):
    def get(self, *args, **kwargs):
        # TODO: Remover delete session
        # if self.request.session.get('car'):
        #     del self.request.session['car']
        #     self.request.session.save()

        http_referer = self.request.META.get(
            'HTTP_REFERER'
        )
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            messages.error(self.request, 'Produto não existe')
            return redirect(http_referer)

        variation = get_object_or_404(Variation, id=variation_id)
        variation_stock = variation.stock
        product = variation.product

        product_id = product.id
        product_name = product.name
        variation_name = variation.name or ''
        unit_price = variation.price
        unit_promotion_price = variation.promotion_price
        quantity = 1
        slug = product.slug
        image = product.image

        if image:
            image = image.name
        else:
            image = ''

        if variation.stock < 1:
            messages.error(self.request, 'Estoque insuficiente!')
            return redirect(http_referer)

        if not self.request.session.get('car'):
            self.request.session['car'] = {}
            self.request.session.save()

        car = self.request.session['car']

        if variation_id in car:
            quantity_car = car[variation_id]['quantity']
            quantity_car += 1

            if variation_stock < quantity_car:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantity_car}x no '
                    f'produto "{product_name}". Adicionamos {variation_stock}x '
                    f'no seu carrinho.'
                )
                quantity_car = variation_stock

            car[variation_id]['quantity'] = quantity_car
            car[variation_id]['quantity_price'] = unit_price * quantity_car
            car[variation_id]['quantity_promotion_price'] = \
                unit_promotion_price * quantity_car

        else:
            car[variation_id] = {
                'product_id': product_id,
                'product_name': product_name,
                'variation_name': variation_name,
                'variation_id': variation_id,
                'unit_price': unit_price,
                'unit_promotion_price': unit_promotion_price,
                'quantity_price': unit_price,
                'quantity_promotion_price': unit_promotion_price,
                'quantity': quantity,
                'slug': slug,
                'image': image,
            }

        self.request.session.save()
        messages.success(
            self.request,
            f'Produto {product_name} {variation_name} adcionado ao seu '
            f'carrinho {car[variation_id]["quantity"]}x'
        )
        return redirect(http_referer)


class RemoveCar(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:list')
        )
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            return redirect(http_referer)

        if not self.request.session.get('car'):
            return redirect(http_referer)

        if variation_id not in self.request.session['car']:
            return redirect(http_referer)

        car = self.request.session['car'][variation_id]

        messages.success(
            self.request,
            f'Produto {car["product_name"]} {car["variation_name"]} '
            f'removido do seu carinho.'
        )

        del self.request.session['car'][variation_id]
        self.request.session.save()
        return redirect(http_referer)


class Car(View):
    def get(self, *args, **kwargs):
        context = {
            'car': self.request.session.get('car', {})
        }
        pprint(context)
        return render(self.request, 'product/car.html', context)


class Finally(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizando')
