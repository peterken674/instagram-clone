from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    name= 'Peter'
    return render(request, 'index.html', {'name':name})