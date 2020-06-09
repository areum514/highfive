from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def publication_page(request):
    links = models.Link.objects.all()
    publications = models.Publication.objects.all()
    pub = models.Publication
    print(vars(publications.model))
    return render(request, 'publication.html', context={"links": links, "publications": publications, "pub": pub})
