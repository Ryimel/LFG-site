from django.shortcuts import render
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^create', include('create.urls')),
    url(r'^', views.home),
]