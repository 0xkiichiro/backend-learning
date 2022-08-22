from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("hello master.")

def fscohort(request):
    return HttpResponse("FS Cohort")

def subfolder(request):
    return HttpResponse("ur @ subfolder")