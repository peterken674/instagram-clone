from app.models import Post
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def register_user(request):
    form = CreateUserForm
    title = 'New Account'

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form, 'title': title}
    return render(request, 'accounts/registration.html', context)


def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')


    context = {}
    return render(request, 'accounts/login.html', context)


def logout(request):
    return render(request, 'accounts/login.html')
