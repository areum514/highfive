from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    return render(request, 'base.html')


def publication_page(request):
    return render(request, 'publication.html')


def reserch_page(request):
    return render(request, 'reserch.html')


def equitment_page(request):
    return render(request, 'equitment.html')
