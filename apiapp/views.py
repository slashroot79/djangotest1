from django.shortcuts import render

from django.http import HttpResponse

def root(request):
    return HttpResponse('<h3>Sample response from api app....</h3>')