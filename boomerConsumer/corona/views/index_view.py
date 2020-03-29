from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from ..models import Boomer, Requests, Zoomer
from django.db import connection
from django.contrib.auth import authenticate
from corona.forms import*
from django.contrib.auth import login as loginDjango
import datetime

def index(request):
    return render(request, 'homepage/index.html',{})

def login(request):
    return render(request, 'login/index.html',{})

def signupB(request):
    if request.method == 'POST':
        form = UserForm(request.POST, prefix='UF')

        if form.is_valid():
            user = form.save(commit=False)
            user.refresh_from_db()
            user.profile.displayName = form.cleaned_data.get('displayName')
            user.save(commit=False)
            user.profile.lastName = form.cleaned_data.get('lastName')
            user.save(commit=False)
            user.profile.age = form.cleaned_data.get('age')
            user.save(commit=False)
            user.profile.email = form.cleaned_data.get('email')
            user.save(commit=False)
            user.profile.phone = form.cleaned_data.get('phoneNumber')
            user.save(commit=False)
            user.profile.postalCode = form.cleaned_data.get('postalCode')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'login/boomer_signup.html',{'form': form})

def signupZ(request):
    return render(request, 'login/zoomer_signup.html',{})



    # Boomer.object.filter(pk="whatever they enter")

    # def signup(request):
    
    # return render(request, 'signup.html', {'form': form})
def boomerIndex(request):
    return render(request, 'homepage/boomerIndex.html',{})

def signupZoomerConfirm(request):
    #find latitude and longitude using jacobs function
    newZoomer= Zoomer(username= request.POST['username'], password=request.POST['password'], name=request.POST['name'], surname=request.POST['surname'],age=request.POST['age'],email=request.POST['email'], postal_code=request.POST['postalcode'],phone=request.POST['phone'],address=request.POST['address'])
    newZoomer.save()
    request.session['username'] = request.POST['username']
    request.session['type'] = 'zoomer'
    return index(request)

def loginSubmit(request):
    try:
        b = Boomer.objects.get(pk=request.POST['username'])
        if(b.password == request.POST['password']):
            request.session['username'] = request.POST['username']
            request.session['type'] = 'boomer'
            return boomerIndex(request)
        else:
            return render(request, 'login/index.html',{'error_message':'Wrong password'})
    except:
        try:
            z = Zoomer.objects.get(pk=request.POST['username'])
            if(z.password == request.POST['password']):
                request.session['username'] = request.POST['username']
                request.session['type'] = 'zoomer'
                return index(request)
            else:
                return render(request, 'login/index.html',{'error_message':'Wrong password'})
        except:
            return render(request, 'login/index.html',{'error_message':'User not registered. Sign up first'})