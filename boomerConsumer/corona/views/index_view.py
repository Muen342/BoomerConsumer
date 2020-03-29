from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from ..models import Boomer, Requests, Zoomer
from django.db import connection
from django.contrib.auth import authenticate

from django.contrib.auth import login as loginDjango
import datetime

def index(request):
    return render(request, 'homepage/index.html',{})

def login(request):
    return render(request, 'login/index.html',{})


def signupZ(request):
    return render(request, 'login/zoomer_signup.html',{})

def signupB(request):
    return render(request, 'login/boomer_signup.html',{})

def boomerIndex(request):
    return render(request, 'homepage/boomerIndex.html',{})

def signupZoomerConfirm(request):
    #find latitude and longitude using jacobs function
    newZoomer= Zoomer(username= request.POST['username'], password=request.POST['password'], name=request.POST['name'], surname=request.POST['surname'],age=request.POST['age'],email=request.POST['email'], postal_code=request.POST['postalcode'],phone=request.POST['phone'],address=request.POST['address'])
    newZoomer.save()
    request.session['username'] = request.POST['username']
    request.session['type'] = 'zoomer'
    return index(request)

def signupBoomerConfirm(request):
    #find latitude and longitude using jacobs function
    newBoomer= Boomer(username= request.POST['username'], password=request.POST['password'], name=request.POST['name'], surname=request.POST['surname'],age=request.POST['age'],email=request.POST['email'], postal_code=request.POST['postalcode'],phone=request.POST['phone'],address=request.POST['address'])
    newBoomer.save()
    request.session['username'] = request.POST['username']
    request.session['type'] = 'boomer'
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