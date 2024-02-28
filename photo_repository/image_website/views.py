from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    return render(request, 'home.html')


def gallery_one(request):
    return render(request, 'gallery_one.html')

def gallery_two(request):
    return render(request, 'gallery_two.html')

def gallery_three(request):
    return render(request, 'gallery_three.html')