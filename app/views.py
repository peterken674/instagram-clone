from app.models import Post
from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    posts = Post.objects.all()

    return render(request, 'index.html', {'posts':posts})