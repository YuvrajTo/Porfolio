from django.http import HttpResponse
from django.shortcuts import render

def stories(request):
    return HttpResponse("Stories")

def nature(request):
    return HttpResponse("Nature")

def birds(request):
    return HttpResponse("Birds")