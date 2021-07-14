from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title', 'description') 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post','user']
        