from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from product.models import Variation
from utils import utils
from .models import Order, OrderItem


class Buy(View):
    template_name = 'order/buy.html'

    def get(self, *args, **kwargs):

        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Você precisa fazer login.'
            )
            return redirect('profile:create')

        if not self.request.session.get('car'):
            messages.error(
                self.request,
                'Carrinho vazio.'
            )
            return redirect('product:list')

        car = self.request.session.get('car')
        car_variation_ids = [v for v in car]

        db_variations = list(
            Variation.objects.select_related(
                'product'
            ).filter(id__in=car_variation_ids)
        )

        for variation in db_variations:
            vid = str(variation.id)

            stock = variation.stock
            qtd_car = car[vid]['quantity']
            unit_price = car[vid]['unit_price']
            unit_promotion_price = car[vid]['unit_promotion_price']

            error_message_stock = ''

            if stock < qtd_car:
                car[vid]['quantity'] = stock
                car[vid]['quantity_price'] = stock * unit_price
                car[vid]['quantity_promotion_price'] = stock * \
                    unit_promotion_price

                error_message_stock = 'Estoque insuficente para alguns produtos' \
                    ' do seu carrinho. Reduzimos a quantidade desse produtos. ' \
                    'Por favor, verique quais produtos foram afetados a seguir.'

                messages.error(
                    self.request,
                    error_message_stock
                )
                self.request.session.save()
                return redirect('product:car')

        qtd_total_car = utils.cart_total_qtd(car)
        value_total_car = utils.cart_totals(car)

        order = Order(
            user=self.request.user,
            total=value_total_car,
            qtd_total=qtd_total_car,
            status='C',
        )

        order.save()

        OrderItem.objects.bulk_create(
            [
                OrderItem(
                    order=order,
                    product=v['product_name'],
                    product_id=v['product_id'],
                    variation=v['variation_name'],
                    variation_id=v['variation_id'],
                    price=v['quantity_price'],
                    promotional_price=v['quantity_promotion_price'],
                    quantity=v['quantity'],
                    image=v['image'],
                ) for v in car.values()
            ]
        )

        del self.request.session['car']
        
        return redirect('order:list')


class SaveOrder(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Fechar Pedido')


class List(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista')


class Details(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhes')
