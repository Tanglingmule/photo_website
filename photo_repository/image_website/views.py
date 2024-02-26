from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    return render(request, 'home.html')


def gallery_one(request):
    return render(request, 'gallery_one.html')