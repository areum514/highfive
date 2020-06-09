from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.


def equitment_page(request):

    photos = models.Photo.objects.all()
    equiptments = models.Equiptment.objects.all()

    return render(request, "equitment.html", context={"equiptments": equiptments, "photos": photos, })
