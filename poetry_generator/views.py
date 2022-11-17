from django.shortcuts import render
from .poem import Poem
# Create your views here.
from django.http import HttpResponse


def index(request):
    poem = Poem()
    poem.speech_output(request)
    poem = poem.tokenize()
    print(poem)
    return render(request, './templates/home.html', {"poem": poem})