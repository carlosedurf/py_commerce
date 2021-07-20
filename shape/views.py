from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class Create(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Criando')


class Update(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizando')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Saindo')
