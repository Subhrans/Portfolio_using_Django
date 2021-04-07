from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SubscribeForm, ContactUsForm
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    MyDetail,
    Subscribe,
    MailBackend,
)


# Create your views here.


def index(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            email = subscribe_form.cleaned_data['email']
            name = email.split('@')[0]
            backend = MailBackend.objects.get(user=request.user)
            if backend.user.is_superuser:
                send_mail(
                    subject="Subscribed User",
                    message="Thanks For subscribing us",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER, email],
                )
            else:
                send_mail(
                    subject="Subscribed User",
                    message="Thanks For subscribing us",
                    from_email=backend.gmail,
                    recipient_list=[backend.gmail, email],
                    auth_user=backend.gmail, auth_password=backend.password
                )
            Subscribe.objects.create(name=name, email=email)
            print("user email is: ", email)
            return render(request, 'portfolio/subscribe_successful.html', {'name': name, "email": email,'backend':backend})
    else:
        subscribe_form = SubscribeForm()
    if request.user.is_anonymous:
        myprofile = MyDetail.objects.filter(user=1)
    else:
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
            backend = MailBackend.objects.get(user=request.user)
            msg = cuform.cleaned_data['query']
            user = cuform.cleaned_data['email']
            if backend.user.is_superuser:
                send_mail(subject='query',
                          message=msg,
                          from_email=settings.EMAIL_HOST_USER,
                          recipient_list=[user, settings.EMAIL_HOST_USER],
                          )
            else:
                send_mail(subject='query',
                          message=msg,
                          from_email=backend.gmail,
                          recipient_list=[user, backend.gmail],
                          auth_user=backend.gmail, auth_password=backend.password
                          )
            cuform.save()
            return HttpResponseRedirect('/contact_us/')
    else:
        cuform = ContactUsForm()
    if request.user.is_anonymous:
        mydetail=MyDetail.objects.filter(user=1)
    else:
        mydetail=MyDetail.objects.filter(user=request.user)
    context = {'i': cuform,"mydetail":mydetail}

    return render(request, 'portfolio/contact.html', context)
