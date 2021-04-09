from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import SubscribeForm, ContactUsForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    MyDetail,
    Subscribe,
    MailBackend,
    Project,
)


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
            return render(request, 'portfolio/subscribe_successful.html',
                          {'name': name, "email": email, 'backend': backend})
    else:
        subscribe_form = SubscribeForm()
    if request.user.is_anonymous:
        myprofile = MyDetail.objects.filter(user=1)
    else:
        myprofile = MyDetail.objects.filter(user=request.user)
    language_used = set()
    for i in myprofile:
        for j in i.projects_detail.all():
            language_used.add(str(j.language_used))
    print(language_used)
    context = {
        'myprofile': myprofile,
        'subscribe_form': subscribe_form,
        'language_used': language_used,

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
        mydetail = MyDetail.objects.filter(user=1)
    else:
        mydetail = MyDetail.objects.filter(user=request.user)
    context = {'i': cuform, "mydetail": mydetail}

    return render(request, 'portfolio/contact.html', context)


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            login_form = LoginForm(request=request.POST, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                validate = authenticate(username=username, password=password)  # it return none if user not found
                if validate is not None:
                    login(request, validate)
                    return HttpResponseRedirect('/')
            else:
                messages.error(request, "Invalid Credentials")
        else:
            login_form = LoginForm()
    else:
        return HttpResponseRedirect('/')
    context = {
        'lform': login_form,
    }
    return render(request, 'portfolio/login.html', context)


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def portfolio_view(request, userid):
    myprofile = MyDetail.objects.filter(user__username=userid)  # userid is basically username
    if not myprofile.exists():
        return HttpResponseNotFound("Page not found")
    context = {
        'myprofile': myprofile
    }
    return render(request, 'portfolio/home.html', context)
