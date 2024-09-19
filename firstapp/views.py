from django.shortcuts import render
from django.http import HttpResponse

def home(request): 
    message = '<h1> Hi rubi </h1>'
    return HttpResponse(message)

# Create your views here.
#http://127.0.0.1:8000/wish
#http response
#14 datatypes

  