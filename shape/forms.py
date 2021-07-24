from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)


class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha'
    )

    password_confirmation = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirme sua Senha'
    )

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
            'password_confirmation',
            'email'
        )

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_messages = {}

        user_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password_confirmation_data = cleaned.get('password_confirmation')

        user_db = User.objects.filter(username=user_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_message_user_exists = 'Usuário já existe'
        error_message_email_exists = 'E-mail já existe'
        error_message_password_match = 'As duas senhas não conferem'
        error_message_password_short = 'Sua senha precisa de pelo menos 6 caracteres'

        # usuários logados: atualização
        if self.user:
            if user_db:
                if user_data != user_db.username:
                    validation_error_messages['username'] = error_message_user_exists

            if email_db:
                if email_data != email_db.email:
                    validation_error_messages['email'] = error_message_email_exists

            if password_data:
                if password_data != password_confirmation_data:
                    validation_error_messages['password'] = error_message_password_match
                    validation_error_messages['password_confirmation'] = error_message_password_match

                if len(password_data) < 6:
                    validation_error_messages['password'] = error_message_password_short

        # usuários não logados: cadastro
        else:
            pass

        if validation_error_messages:
            raise(forms.ValidationError(validation_error_messages))
