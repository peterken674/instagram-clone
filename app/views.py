from app.models import Post
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def register(request):
    form = CreateUserForm
    title = 'New Account'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form, 'title': title}
    return render(request, 'accounts/registration.html', context)


def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)


def logout(request):
    return render(request, 'accounts/login.html')
