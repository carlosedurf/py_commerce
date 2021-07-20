from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class ListProduct(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Listando produtos')


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
