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
from .nonboomer_view import show_requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import math
import requests
from itertools import cycle
import traceback
from lxml.html import fromstring
import time
import json

def nearestPostalCode():
    return "hello world"


def my_function():
    print("Hello World")

def testFunc():
    raw_html = open('contrived.html').read()
    html = BeautifulSoup(raw_html, 'html.parser')
    for p in html.select('p'):
        if p['id'] == 'walrus':
            print(p.text)

# def parsePostal(postalCode): 
#     url = "http://www.zip-codes.com/canadian/postal-code.asp?postalcode=" + postalCode.lower().replace(" ", "")
#     raw_html = simple_get(url)
    
#     if raw_html is not None:
#         raw_text = ''
#         html =  BeautifulSoup(raw_html, 'html.parser')
#         for td in html.select('td'):
#             raw_text += td.text
        
#         lat_split = raw_text.lower().split('latitude')
#         lat_split = lat_split[2].split('elevation')[0]
#         latitude =  lat_split.split(':')[1].split('longitude')[0]
#         longitude = lat_split.split('longitude:')[1]

#         print("latitude: " + latitude)
#         print("longitude: " + longitude)

#         lat_long_list = [float(latitude), float(longitude)]
#         return lat_long_list

           
#     else:
#         print("No data found for that postal code")
#         return [None,None]

#https://geocoder.ca/?locate=l8v4x5&geoit=XML&json=1

def parsePostal(postalCode):
    time.sleep(2)
    print(postalCode) 
    url = "https://geocoder.ca/?locate=" + postalCode.lower().replace(" ", "") + "&geoit=XML&json=1"
    
    try:
        response = requests.get(url)
    except:
        print("Skipping. Connnection error")
        return [None, None]
    #print(response.json())
    data = response.json()
    data = json.dumps(data)
    #print(data)
    longitude = data.split('longt')[1].split('": "')[1].split('",')[0]
    latitude = data.split('latt')[1].split('": "')[1].split('"}')[0]
    #print('latitude: ' + latitude)
    #print('longitude: ' + longitude)
    return float(latitude), float(longitude)

def index(request):
    return show_requests(request)

def login(request):
    return render(request, 'login/index.html',{})


def signupZ(request):
    return render(request, 'login/zoomer_signup.html',{})

def signupB(request):
    return render(request, 'login/boomer_signup.html',{})

def boomerIndex(request):
    return show_requests(request)

def signupZoomerConfirm(request):
    lat,longi  = parsePostal(request.POST['postalcode'])
    newZoomer= Zoomer(username= request.POST['username'], password=request.POST['password'], name=request.POST['name'], surname=request.POST['surname'],age=request.POST['age'],email=request.POST['email'], postal_code=request.POST['postalcode'],phone=request.POST['phone'],address=request.POST['address'],latitude=lat,longitude=longi)
    newZoomer.save()
    request.session['username'] = request.POST['username']
    request.session['type'] = 'zoomer'
    return index(request)

def signupBoomerConfirm(request):
    lat,longi  = parsePostal(request.POST['postalcode'])
    newBoomer= Boomer(username= request.POST['username'], password=request.POST['password'], name=request.POST['name'], surname=request.POST['surname'],age=request.POST['age'],email=request.POST['email'], postal_code=request.POST['postalcode'],phone=request.POST['phone'],address=request.POST['address'],latitude=lat,longitude=longi)
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
def logout(request):
    del request.session['username']
    del request.session['type']
    return login(request)