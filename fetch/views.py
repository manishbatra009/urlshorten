from django.shortcuts import render
from django.http import HttpResponse
from . import CsrfExemptSessionAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.views.decorators.csrf import csrf_exempt
import json
from .models import URLS
from django.http import JsonResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError



#authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
def url_shortify(longurl):
    return

def url_verify(longurl):
    val = URLValidator(verify_exists=False)
    if val(longurl):
        return True
    else:
        return False

@csrf_exempt
def short_url(request):

    longurl = json.loads(request.body)[long_url]
    if url_verify(longurl):
        if URLS.objects.get(longURL=longurl):
            u = URLS.objects.get(longURL=longurl)
            return JsonResponse({'short_url': u.shortURL})
        else:
            shorturl = url_shortify(longurl)
            u = URLS()
            u.longURL=longurl
            u.shortURL=shorturl
            return JsonResponse({'short_url': shorturl})
    else:
        return HttpResponse("error")


@csrf_exempt
def long_url(request):

    shorturl = json.loads(request.body)[short_url]
    if URLS.objects.get(shortURL = shorturl):
        u = URLS.objects.get(shortURL = shorturl)
        return JsonResponse({'long_url': u.longURL})
    else:
        return HttpResponse("error")



@csrf_exempt
def short_urls(request):
    longurls = json.loads(request.body)[long_url]
    return HttpResponse("3")

@csrf_exempt
def long_urls(request):
    return HttpResponse("4")

def count(request):
    shorturl = json.loads(request.body)[short_url]
    if URLS.objects.get(shortURL=shorturl):
        u = URLS.objects.get(shortURL=shorturl)
        return JsonResponse({'count':u.count})
    else:
        return HttpResponse("error")


def index(request):
    return HttpResponse("0")
# Create your views here.
