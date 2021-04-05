from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SubscribeForm, ContactUsForm
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    MyDetail,
    Post_Graduation,
    Subscribe,
    Higher_Secondary_Examination,
    Secondary_Examination,
    Social_Site_Connection,
    Achievment,
    Project,
    Qualification,
    Under_Graduation,
    ContactUs,
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
    myprofile = MyDetail.objects.all()
    projects = Project.objects.all()
    social_links = Social_Site_Connection.objects.all()
    context = {
        'myprofile': myprofile,
        'subscribe_form': subscribe_form,
        'projects': projects,
        "social_links": social_links,

    }

    return render(request, 'portfolio/home.html', context)


def contact_us_view(request):
    if request.method == "POST":
        cuform = ContactUsForm(request.POST)
        if cuform.is_valid():
            msg=cuform.cleaned_data['query']
            user=cuform.cleaned_data['email']
            send_mail(subject='query',
                      message=msg,
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[user,settings.EMAIL_HOST_USER],
                      )
            cuform.save()
            return HttpResponseRedirect('/contact_us/')
    else:
        cuform = ContactUsForm()

    context={'i':cuform}

    return render(request,'portfolio/contact.html',context)