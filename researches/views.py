from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def research_page(request):

    researches = models.Research.objects.all()

    return render(request, "research.html", context={"researches": researches, })
