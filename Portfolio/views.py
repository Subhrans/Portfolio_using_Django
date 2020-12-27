from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request,'base.html',context=None)
def index(request):
    return render(request,'portfolio/home.html',context=None)