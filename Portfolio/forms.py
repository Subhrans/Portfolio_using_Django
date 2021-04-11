from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Subscribe, ContactUs, MailBackend


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']
        widgets = {'email': forms.EmailInput(attrs={'class': 'user-email form-control',
                                                    'id': 'user-email',
                                                    'placeholder': 'Email',
                                                    }),
                   }


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control mt-4'
            }),
            'query': forms.Textarea(attrs={
                'class': 'form-control overflow-scroll',
                'rows': 5,
            })
        }


# class ContactBackendForm(forms.ModelForm):
#     class Meta:
#         model = MailBackend
#         fields = ['user', 'gmail', 'password']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'password']
