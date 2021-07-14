from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login_user, name='login'),
    path('accounts/register/', views.register_user, name='register'),
    path('accounts/logout/', views.logout_user, name='logout'),
    path('new_post/', views.new_post, name='new_post'),

]
