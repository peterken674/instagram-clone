from django.http.response import Http404
from app.models import Post, Comment, Profile, Like
from django.shortcuts import redirect, render
from .forms import CreateUserForm, UploadImageForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
import json

from django.contrib import messages

@login_required(login_url='login')
def index(request):

    posts = Post.objects.all()
    liked_posts = [i for i in Post.objects.all() if Like.objects.filter(user = request.user, post=i)]

    if request.method == 'POST':
        upload_form = UploadImageForm(request.POST, request.FILES)
        
        if upload_form.is_valid():
            upload_form.instance.user = request.user.profile
            upload_form.save()

            return redirect('index')

    else:
        upload_form = UploadImageForm()

    context = {'upload_form': upload_form, 'posts':posts, 'liked_posts': liked_posts, 'range':range(1,4)}

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

def comment(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment_form.instance.user = request.user.profile
            comment_form.instance.post = post

            comment_form.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def like(request, post_id):
    user = request.user
    post = Post.objects.get(pk=post_id)
    liked= False
    like = Like.objects.filter(user=user, post=post)
    if like:
        like.delete()
    else:
        liked = True
        new_like = Like(user=user, post=post)
        new_like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        