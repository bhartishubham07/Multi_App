from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def APP2_first(request):
    return HttpResponse('<h1>This is first function of APP2</h1>')

def APP2_second(request):
    return HttpResponse('<h1>This is second function of APP2</h1>')