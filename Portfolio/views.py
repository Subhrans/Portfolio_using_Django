from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SubscribeForm, ContactUsForm
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    MyDetail,
    Subscribe,
)


# Create your views here.


def index(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            email = subscribe_form.cleaned_data['email']
            name = email.split('@')[0]
            send_mail(
                subject="Subscribed User",
                message="Thanks For subscribing us",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER, 'subhransud525@gmail.com'],
            )
            Subscribe.objects.create(name=name, email=email)
            print("user email is: ", email)
            return render(request, 'portfolio/subscribe_successful.html', {'name': name, "email": email})
    else:
        subscribe_form = SubscribeForm()
    myprofile = MyDetail.objects.filter(user=request.user)
    context = {
        'myprofile': myprofile,
        'subscribe_form': subscribe_form,

    }

    return render(request, 'portfolio/home.html', context)


def contact_us_view(request):
    if request.method == "POST":
        cuform = ContactUsForm(request.POST)
        if cuform.is_valid():
            msg = cuform.cleaned_data['query']
            user = cuform.cleaned_data['email']
            send_mail(subject='query',
                      message=msg,
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[user, settings.EMAIL_HOST_USER],
                      )
            cuform.save()
            return HttpResponseRedirect('/contact_us/')
    else:
        cuform = ContactUsForm()

    context = {'i': cuform}

    return render(request, 'portfolio/contact.html', context)
