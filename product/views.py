from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from .models import Product


class ListProduct(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 9


class ProductDetails(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhes do Produto')


class AddCar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar ao carrinho')


class RemoveCar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Removendo do carrinho')


class Car(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finally(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizando')
