from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, './templates/home.html')

def speech_output(request):
    data=request.get