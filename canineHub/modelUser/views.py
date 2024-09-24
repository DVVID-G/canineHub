from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    
    if request.method == 'GET':
        return render(request, 'register.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('task')
            except IntegrityError:
                return render(request,'register.html', {'form': UserCreationForm, 'error': 'Username is already taken'})
        else:
            return render(request,'register.html', {'form': UserCreationForm, 'error': 'Passwords did not match'})
        

def task(request):
    return render(request, 'task.html')

def logoutuser(request):
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm, 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('task')
    
            

