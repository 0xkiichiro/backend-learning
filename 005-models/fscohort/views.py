from django.shortcuts import render
from django.http import HttpResponse

# views returns a function. right now its just printing on html but in the futurue it will go to the database, fetch the data requested and print it
def home(request):
    return HttpResponse("oi")