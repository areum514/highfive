from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.


def member_page(request):
    # return HttpResponse(content="hello")
    all_members = models.Member.objects.all()

    return render(request, "people.html", context={"members": all_members, })
