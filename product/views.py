from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse, request
from django.contrib import messages
from django.urls import reverse
from .models import Product, Variation


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
        http_referer = self.request.META.get(
            'HTTP_REFERER'
        )
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            messages.error(self.request, 'Produto não existe')
            return redirect(http_referer)

        variation = get_object_or_404(Variation, id=variation_id)

        if not self.request.session.get('car'):
            self.request.session['car'] = {}
            self.request.session.save()

        car = self.request.session['car']

        if variation_id in car:
            # TODO: Variation exists in car
            pass
        else:
            # TODO: Variation not exists in car
            pass

        return HttpResponse(f'{variation.product} {variation.name}')


class RemoveCar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Removendo do carrinho')


class Car(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finally(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizando')
