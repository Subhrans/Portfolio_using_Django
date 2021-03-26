from django import forms
from django.core import validators
from .models import Subscribe


class SubscribeForm(forms.Form):
    class Meta:
        model = Subscribe
        fields = ['email']
        widgets = forms.EmailInput(attrs={'class': 'user-email form-control',
                                          'id': 'user-email',
                                          'placeholder': 'Email',
                                          })

    # email = forms.EmailField(label="Email",
    #                          label_suffix="",
    #                          validators=[validators.EmailValidator],
    #                          widget=forms.EmailInput(attrs={'class': 'user-email form-control',
    #                                                         'id': 'user-email',
    #                                                         'placeholder': 'Email',
    #                                                         }))
