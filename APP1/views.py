from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def APP1_first(request):
    return HttpResponse('<h1><marquee>This is first function of APP1</marquee></h1>')

def APP1_second(request):
    return HttpResponse('<h1><marquee>This is second function of APP1</marquee></h1>')