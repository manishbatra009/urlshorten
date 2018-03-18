from django.shortcuts import render
from django.http import HttpResponse
from . import CsrfExemptSessionAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

def short_url(request):
    if request.method == 'POST':
        return HttpResponse(request.body)
def short_urls(request):
    return HttpResponse("2")
def long_url(request):
    return HttpResponse("3")
def long_urls(request):
    return HttpResponse("4")
def count(request):
    return HttpResponse("5")
def verify(request):
    return HttpResponse("6")

def index(request):
    return HttpResponse("0")
# Create your views here.
