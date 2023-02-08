from .models import *
from django.forms import ModelForm, TextInput
from django import forms
from django.core.exceptions import ValidationError


class CustomUserForm(ModelForm):

    class Meta:

        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password',]
        widgets = {
            'username': TextInput(attrs={
                'type': "text",  'placeholder': "login"
            }),
            'email': TextInput(attrs={
                'type': "email",  'placeholder': "email"
            }),
            'confirm_password': TextInput(attrs={
                'type': "password",  'placeholder': "********"
            }),
            'password': TextInput(attrs={
                'type': "password",  'placeholder': "********"
            }),
        }

    # Проверка почты на валидность
    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if CustomUser.objects.filter(email__iexact=email).exists():
            raise ValidationError('Это почта уже используется!')
        return email
    
    # Проверка имени на валидность
    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if CustomUser.objects.filter(username__iexact=username).exists():
            raise ValidationError('Это имя уже используется!')
        if username.isalnum():
            for i in set(username):
                if ord(i) > 177:
                    raise ValidationError('Используйте латинские буквы!')
        else:
            raise ValidationError('Используйте цифры от 0-9, "_" и "-".')
        return username

    # Проверка пароля на валидность
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password'].strip()
        password = self.cleaned_data['password'].strip()
        if password != confirm_password:
            raise ValidationError('Пароли не совпадают!')
        if len(password) < 12:
            raise ValidationError('Слишком короткий пароль!')
        if len(set(password)) < 5:
            raise ValidationError('Пароль слишком простой!')
        if password.isalpha() or password.isdigit():
            error = ['Цифры от 0-9', 'минимум одну сточную и одну заглавную букву']
            raise ValidationError(f'Пароль должен содеражать {error[password.isdigit()]}')
        test_arg = [0, 0]
        for i in password:
            if 'a' <= i.lower() <= 'z':
                if i.isupper():
                    test_arg[1] = 1
                else:
                    test_arg[0] = 1
        if sum(test_arg) != 2:
            error = ['строчную букву', 'заглавную букву']
            raise ValidationError(f'пароль должен соджержать {error[test_arg.index(0)]}')
        return password


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'login'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': '********'}))
