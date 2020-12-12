from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from users.forms.login_form import LoginForm
from users.forms.register_form import RegisterForm
from users.forms.results_form import ResultsForm
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
    user = User.objects.get(id=pk)
    results_bulk = user.registereduser.results_set.all()

    context = {'user': user, 'results_bulk': results_bulk}

    return render(request, 'users/profile_page.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
def add_results(request):
    if request.method == 'GET':
        form = ResultsForm()
        context = {
            'form': form,
        }
        return render(request, 'users/add_results.html', context)
    else:

        form = ResultsForm(request.POST)
        if form.is_valid():
            results = form.save(commit=False)
            results.user = RegisteredUser.objects.get(user=request.user)
            results.save()
            return redirect('/')
        else:
            context = {
                'form': form,
            }
            return render(request, 'users/add_results.html', context)


@login_required
def edit_results(request, pk):
    results_bulk = Results.objects.get(id=pk)
    if request.method == "GET":
        form = ResultsForm(instance=results_bulk)
        context = {'form': form, 'results_bulk': results_bulk}

        return render(request, 'users/edit_results.html', context)
    else:
        form = ResultsForm(request.POST, instance=results_bulk)
        if form.is_valid():
            form.save()
            return redirect('/', results_bulk.pk)
        else:
            context = {'form': form, 'results_bulk': results_bulk}
            return render(request, 'users/edit_results.html', context)


@login_required
def delete_results(request, pk):
    results_to_delete = Results.objects.get(id=pk)
    if request.method == 'GET':
        context = {'results_to_delete': results_to_delete}

        return render(request, 'users/delete_results.html', context)

    else:
        results_to_delete.delete()
        return redirect('/')



