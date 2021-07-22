from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class Buy(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')


class SaveOrder(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Fechar Pedido')


class Details(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhes')
