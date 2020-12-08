from django.shortcuts import render

# Create your views here.


def home(request):

    context = {}

    return render(request, 'measure_app/dashboard.html', context)


def library(request):

    context = {}

    return render(request, 'measure_app/library.html', context)
