from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def register_view(request):
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        newUser = User(username=username)
        newUser.set_password(password)
        
        newUser.save()
        login(request, newUser)
        
        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm(request=request)
    
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
