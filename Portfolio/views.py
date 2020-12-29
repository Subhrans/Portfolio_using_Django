from django.shortcuts import render
from .forms import subscribe
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
        subs=subscribe()
    return render(request,'portfolio/home.html',context={'form':subs})