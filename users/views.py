from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from users.forms.login_form import LoginForm
from users.forms.register_form import RegisterForm
from users.models import *


def register(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm(),
        }
        return render(request, 'users/register.html', context)
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = RegisteredUser(
                user=user,
            )
            profile.save()
            login(request, user)
            return redirect('/')
        context = {
            'form': form,
        }
        return render(request, 'users/register.html', context)


def login_user(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm()
        }
        return render(request, 'users/login.html', context)
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
        context = {
            'form': form,
        }

        return render(request, 'users/login.html', context)


def profile_page(request, pk):
    results_type = Results.objects.all()
    user = User.objects.get(pk=pk)

    context = {'results_type': results_type, 'user': user}

    return render(request, 'users/profile_page.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')

