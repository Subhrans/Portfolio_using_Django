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
    Service,
)

local_visited = False


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
        service = Service.objects.filter(user=1)
    else:
        myprofile = MyDetail.objects.filter(user=request.user)
        service = Service.objects.filter(user=request.user)
        check_visited = request.session.get('visited', 'False')
        if check_visited == "True":
            myprofile.update(visited=True)
        if len(myprofile) == 0:
            request.session['visited'] = "False"
        if len(myprofile) == 1:
            request.session['visited'] = "True"
    language_used = set()
    for i in myprofile:
        for j in i.projects_detail.all():
            language_used.add(str(j.language_used))

    context = {
        'myprofile': myprofile,
        'subscribe_form': subscribe_form,
        'language_used': language_used,
        'service': service,

    }
    return render(request, 'portfolio/home.html', context)


def contact_us_view(request, userid=1):
    print("userid is:", userid)
    if request.method == "POST":
        cuform = ContactUsForm(request.POST)
        if cuform.is_valid():
            print("check user anony,ois", request.user.is_anonymous, "userid", userid)
            if request.user.is_anonymous and userid != 1:
                if MailBackend.objects.filter(user__username=userid).exists():
                    backend = MailBackend.objects.get(user__username=userid)
                else:
                    messages.error(request, 'You have not added mail backend. Kindly add that first')
                    backend = None
            elif request.user.is_anonymous and userid == 1:
                backend = MailBackend.objects.get(user=1)
            else:
                backend = MailBackend.objects.get(user=request.user)
            msg = cuform.cleaned_data['query']
            user = cuform.cleaned_data['email']
            if backend:
                print(backend.user)
                print(backend.gmail)
                print(backend.password)
                if backend.user.is_superuser:
                    send_mail(subject='query',
                              message=msg,
                              from_email=settings.EMAIL_HOST_USER,
                              recipient_list=[user, settings.EMAIL_HOST_USER],
                              )
                    cuform.save()
                    messages.success(request, "Mail Query sent successfully")
                    return HttpResponseRedirect('/contact_us/')
                else:
                    send_mail(subject='query',
                              message=msg,
                              from_email=backend.gmail,
                              recipient_list=[user, backend.gmail],
                              auth_user=backend.gmail, auth_password=backend.password
                              )
                    cuform.save()
                    messages.success(request, "Mail Query sent successfully")
                    return HttpResponseRedirect('/'+str(userid)+'/contact_us/')
    else:
        cuform = ContactUsForm()
    print("check user", request.user.is_anonymous)
    if request.user.is_anonymous and userid != 1:
        mydetail = MyDetail.objects.filter(user__username=userid)
    elif request.user.is_anonymous and userid == 1:
        mydetail = MyDetail.objects.filter(user=1)
    else:
        mydetail = MyDetail.objects.filter(user=request.user)

    false_path = None
    if request.path == "/" + str(userid) + '/contact_us/':
        false_path = "/" + str(userid) + '/contact_us/'
    context = {'i': cuform,
               "mydetail": mydetail,
               'false_path':false_path,
               }
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
        'myprofile': myprofile,
    }
    return render(request, 'portfolio/home.html', context)
