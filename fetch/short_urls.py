from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Inside fetch -> short_url")
# Create your views here.
