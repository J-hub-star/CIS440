from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'carrental/index.html')

def about(request):
    return HttpResponse("About")


def profile(request):
    return HttpResponse("Profile")


