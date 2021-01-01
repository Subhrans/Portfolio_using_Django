from django.shortcuts import render
from .forms import subscribe
from .models import (MyDetail,
                     Post_Graduation,
                     subscribe,
                     Higher_Secondary_Examination,
                     Secondary_Examination,
                     Social_Site_Connection,
                     Achievment,
                     Project,
                     Qualification,
                     Under_Graduation,)
# Create your views here.
def base_view(request):
    return render(request,'base.html',context=None)
def index(request):
    if(request.method=='POST'):
        subs=subscribe(request.POST)
        if(subs.is_valid()):
            email=subs.cleaned_data['email']
            print("user email is: ",email)
    else:
        myprofile=MyDetail.objects.all()
        subs=subscribe()
        context={'myprofile':myprofile,'from':subs}
    return render(request,'portfolio/home.html',context)