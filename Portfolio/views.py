from django.shortcuts import render
from .forms import SubscribeForm
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
    # if request.method == 'POST':
    #     subs = SubscribeForm(request.POST)
    #     if subs.is_valid():
    #         email = subs.cleaned_data['email']
    #         print("user email is: ", email)
    # else:
    myprofile = MyDetail.objects.all()
    projects = Project.objects.all()
    subscribe_form = SubscribeForm()
    context = {
        'myprofile': myprofile,
        'subscribe_form': subscribe_form,
        'projects': projects,
    }

    return render(request, 'portfolio/home.html', context)
