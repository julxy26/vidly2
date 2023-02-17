from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """ index """
    return render(request, "home.html", {"home": home})
