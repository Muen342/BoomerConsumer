from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db import connection
import datetime

def index(request):
    #for now
    request.session['username'] = 'mzhang'
    request.session['type'] = 'zoomer'
    return render(request, 'homepage/index.html',{})

def login(request):
    return render(request, 'login/index.html',{})

def signupB(request):
    return render(request, 'login/boomer_signup.html',{})

def signupZ(request):
    return render(request, 'login/zoomer_signup.html',{})

def boomerIndex(request):
    # for now
    request.session['username'] = 'gays'
    request.session['type'] = 'boomer'
    return render(request, 'homepage/boomerIndex.html',{})