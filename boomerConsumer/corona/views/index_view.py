from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db import connection
import datetime

def index(request):
    return render(request, 'homepage/index.html',{})

def login(request):
    return render(request, 'login/index.html',{})

def signup(request):
    return render(request, 'login/boomer_signup',{})