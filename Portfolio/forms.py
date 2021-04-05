from django import forms
from django.core import validators
from .models import Subscribe, ContactUs


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
