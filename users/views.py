from django.shortcuts import render
from .models import Users
# Create your views here.

def home_view(request):
    users=Users.objects.all()
    return render(request,'index.html',{'users':users})