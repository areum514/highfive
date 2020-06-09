from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def research_page(request):
    # return HttpResponse(content="hello")
    photos = models.Photo.objects.all()
    researches = models.Research.objects.all()
    return render(request, "research.html", context={"researches": researches, "photos": photos})
