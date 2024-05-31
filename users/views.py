from django.shortcuts import render
from .models import Users
# Create your views here.

def home_view(request):
    users=Users.objects.all()
    return render(request,'index.html',{'users':users})

def about__view(request):
    return render(request,'about.html')

def contact__view(request):
    return render(request,'contact.html')