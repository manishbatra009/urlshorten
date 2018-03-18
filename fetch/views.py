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
def hash(id):
    cString = "69q4we3r01ty2uiopas7dfghjk8lzxcv5bnm"
    if id < 36:
        return cString[id]
    else:
        return hash(id // 36) + cString[id % 36]

def url_shortify(longurl):
    return hash(URLS.objects.get(longURL = longurl).id)

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
    longurls = json.loads(request.body)[long_urls]
    j={}
    valid=[]
    invalid=[]
    for l in longurls:
        if url_verify(l):
            if URLS.objects.get(longURL=l):
                u = URLS.objects.get(longURL=l)
                j[l] = u.shortURL
            else:
                shorturl = url_shortify(l)
                u = URLS()
                u.longURL = l
                u.shortURL = shorturl
                j[l] = shorturl
        else:
            invalid.append(l)
    if invalid:
        return JsonResponse({'invalid_urls':invalid})
    else:
        return JsonResponse(j)

@csrf_exempt
def long_urls(request):
    shorturls = json.loads(request.body)[short_urls]
    j = {}
    valid = []
    invalid = []
    for s in shorturls:
        if URLS.objects.get(shortURL=s):
            u = URLS.objects.get(shortURL=s)
            j[s] = u.longURL
        else:
            invalid.append(s)
    if invalid:
        return JsonResponse({'invalid_urls': invalid})
    else:
        return JsonResponse(j)


@csrf_exempt
def clean_urls(request):
    URLS.objects.all().delete()
    return JsonResponse({'status': 'success'})

@csrf_exempt
def redirect(request):
    s = hash
    l = URLS.objects.get(shortURL = s).longURL
    return redirect(l)




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
