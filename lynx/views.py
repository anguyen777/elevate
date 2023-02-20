from django.shortcuts import render
from django.http import HttpResponse

# - Homepage

def home(request):

    return HttpResponse('<h1>Demo</h1>')