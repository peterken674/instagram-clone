from app.models import Post, Comment, Profile
from django.shortcuts import redirect, render
from .forms import CreateUserForm, UploadImageForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks     
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect

from django.contrib import messages

@login_required(login_url='login')
def index(request):
    posts = Post.objects.all()

    # if request.method == 'POST':
    #     upload_form = UploadImageForm(request.POST, request.FILES)
        
    #     if upload_form.is_valid():
    #         image = upload_form.cleaned_data.get('image')
    #         title = upload_form.cleaned_data.get('title')
    #         description = upload_form.cleaned_data.get('description')
    #         post = Post(image=image, title=title, description=description, user=current_user)

    #         post.save_post()

    # else:
    #     upload_form = UploadImageForm()

    context = {'posts':posts}

    return render(request, 'index.html',context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
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
    if request.user.is_authenticated:
        return redirect('/')

    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect.')

    context = {}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def new_post(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.instance.user = request.user.profile
            form.save()

            return redirect('index')

        else:
            print(form.errors)

    else:
        form = UploadImageForm()

    context = {'upload_form': form, 'posts':posts}

    return render(request, 'newpost.html', context)


