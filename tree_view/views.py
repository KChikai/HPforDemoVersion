from django.shortcuts import render
from . import APP_LABEL


def index(request):
    return render(request, APP_LABEL + '/index.html')


def embedding(request):
    return render(request, APP_LABEL + '/test_embedding.html')
