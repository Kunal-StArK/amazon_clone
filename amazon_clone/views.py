from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return HttpResponse("hello this is python")