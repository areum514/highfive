from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.


def equitment_page(request):
    equiptments = models.Equiptment.objects.all()
    return render(request, "equitment.html", context={"equiptments": equiptments, })
