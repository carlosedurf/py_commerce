from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from .forms import UserForm, ProfileForm


class BasePerfil(View):
    template_name = 'shape/create.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:
            self.context = {
                'userform': UserForm(
                    data=self.request.POST or None,
                    user=self.request.user,
                    instance=self.request.user
                ),
                'profileform': ProfileForm(
                    data=self.request.POST or None
                )
            }
        else:
            self.context = {
                'userform': UserForm(
                    data=self.request.POST or None
                ),
                'profileform': ProfileForm(
                    data=self.request.POST or None
                )
            }

        self.render = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.render


class Create(BasePerfil):
    def post(self, *args, **kwargs):
        return self.render


class Update(BasePerfil):
    pass


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Saindo')
