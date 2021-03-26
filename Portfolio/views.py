from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SubscribeForm
from django.core.mail import send_mail
from django.conf import settings
from .models import (MyDetail,
                     Post_Graduation,
                     Subscribe,
                     Higher_Secondary_Examination,
                     Secondary_Examination,
                     Social_Site_Connection,
                     Achievment,
                     Project,
                     Qualification,
                     Under_Graduation, )


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
                recipient_list=[settings.EMAIL_HOST_USER,'subhransud525@gmail.com'],
            )
            Subscribe.objects.create(name=name,email=email)
            print("user email is: ", email)
            return HttpResponseRedirect('/')
    else:
        subscribe_form = SubscribeForm()
    myprofile = MyDetail.objects.all()
    projects = Project.objects.all()
    context = {
        'myprofile': myprofile,
        'subscribe_form': subscribe_form,
        'projects': projects,
    }

    return render(request, 'portfolio/home.html', context)
