from django.shortcuts import render
from .poem import Poem
# Create your views here.
from django.http import HttpResponse


def index(request):
    print('check print')
    poem = Poem()
    poem.speech_output(request)
    poem.tokenize()
    return render(request, './templates/home.html')