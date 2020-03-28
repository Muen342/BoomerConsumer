from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db import connection
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as loginDjango
import datetime

def index(request):
    return render(request, 'homepage/index.html',{})

def login(request):
    return render(request, 'login/index.html',{})

def signupB(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            loginDjango(request, user)
            return redirect('homepage/index2') # CHANGE OT WHATEVER NEEDED
    else:
        form = UserCreationForm()
    return render(request, 'login/boomer_signup.html',{'form': form})

def signupZ(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            loginDjango(request, user)
            return redirect('homepage/index2') # CHANGE TO WHATEVER THING NEEDED
    else:
        form = UserCreationForm()
    return render(request, 'login/zoomer_signup.html',{'form': form})



    # Boomer.object.filter(pk="whatever they enter")

    # def signup(request):
    
    # return render(request, 'signup.html', {'form': form})