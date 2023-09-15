from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import UserCreateForm
from django.contrib.auth.decorators import login_required


def account_signup(request):
    if request.method == 'GET':
        return render(request, 'account_signup.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'account_signup.html', {'form': UserCreateForm,
                 'error': 'Username already taken. Choose a different username.'})
        else:
            return render(request, 'account_signup.html', {'form': UserCreateForm, 'error': 'Passwords do not match'})


@login_required
def account_logout(request):
    logout(request)
    return redirect('home')


def account_login(request):
    if request.method == 'GET':
        return render(request, 'account_login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'account_login.html', {'form': AuthenticationForm, 'error': 'Username and Password do not match'})
        else:
            login(request, user)
            return redirect('home')
