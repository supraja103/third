from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def verma(request):
    return HttpResponse('<h1><marquee>worth vermaa..</marquee></h1>')