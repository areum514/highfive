from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def home_page(request):
    CooperativeResearchInstitutions = models.CooperativeResearchInstitution.objects.all()
    return render(request, 'base.html', context={"CooperativeResearchInstitutions": CooperativeResearchInstitutions, })
