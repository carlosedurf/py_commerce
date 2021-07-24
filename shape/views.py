from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from .forms import UserForm, ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import copy


class BasePerfil(View):
    template_name = 'shape/create.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.car = copy.deepcopy(self.request.session.get('car', {}))

        self.profile = None

        if self.request.user.is_authenticated:
            self.profile = Profile.objects.filter(
                user=self.request.user
            ).first()
            self.context = {
                'userform': UserForm(
                    data=self.request.POST or None,
                    user=self.request.user,
                    instance=self.request.user
                ),
                'profileform': ProfileForm(
                    data=self.request.POST or None,
                    instance=self.profile
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

        self.userform = self.context['userform']
        self.profileform = self.context['profileform']

        if self.request.user.is_authenticated:
            self.template_name = 'shape/update.html'

        self.render = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.render


class Create(BasePerfil):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.profileform.is_valid():
            return self.render

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        # usuário logado
        if self.request.user.is_authenticated:
            user = get_object_or_404(User, username=self.request.user.username)
            user.username = username

            if password:
                user.set_password(password)

            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            if not self.profile:
                self.profileform.cleaned_data['user'] = user
                profile = Profile(**self.profileform.cleaned_data)
                profile.save()
            else:
                profile = self.profileform.save(commit=False)
                profile.user = user
                profile.save()

        # usuário não logado (novo)
        else:
            user = self.userform.save(commit=False)
            user.set_password(password)
            user.save()

            profile = self.profileform.save(commit=False)
            profile.user = user
            profile.save()

        if password:
            auth_user = authenticate(
                username=user,
                password=password
            )

            if auth_user:
                login(self.request, user=user)

        self.request.session['car'] = self.car
        self.request.session.save()

        messages.success(
            self.request,
            'Seu cadastro foi criado e/ou atualizado com sucesso!'
        )

        messages.success(
            self.request,
            'Você fez login e pode concluir sua compra!'
        )

        return redirect('profile:create')


class Update(BasePerfil):
    pass


class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('profile:create')

        user = authenticate(
            self.request,
            username=username,
            password=password
        )

        if not user:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('profile:create')

        login(self.request, user=user)
        messages.success(
            self.request,
            'Você fez login no sistema e pode concluir sua compra!'
        )
        return redirect('product:car')


class Logout(View):
    def get(self, *args, **kwargs):
        car = copy.deepcopy(self.request.session.get('car'))
        logout(self.request)
        self.request.session['car'] = car
        self.request.session.save()
        return redirect('product:list')
