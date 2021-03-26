from django import forms
from django.core import validators
from .models import Subscribe
class subscribe(forms.Form):
    email=forms.EmailField(label="Email",
                           label_suffix="",
                           validators=[validators.EmailValidator],
                           widget=forms.EmailInput(attrs={'class':'user-email',
                                                          'id':'user-email',
                                                          'placeholder':'Email',
                                                          }))
