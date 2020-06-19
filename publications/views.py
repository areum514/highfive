from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def publication_page(request):

    publications = models.Publication.objects.all()

    return render(request, 'publication.html', context={"publications": publications, })
