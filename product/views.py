from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from .models import Product


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
