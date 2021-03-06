from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from ..models import Boomer, Requests, Zoomer
from django.urls import reverse
from django.views import generic
from django.db import connection
import datetime
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
def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    #time.sleep(5)
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None



def complex_get(url):
    #print("called simpleget")
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    proxies = get_proxies()
    proxy_pool = cycle(proxies)
    proxy = next(proxy_pool)
    #try:
    
    for i in range(1,len(proxies)):
        
        #Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d"%i)
        try:
            response = get(url, proxies={"http": proxy, "https": proxy})
            #print(response.json())
            #print(response.content)
            if(is_good_response(response)):
                if('elevation' in response.content):   
                    print('good request')
                    return response.content
                else: print('Bad Request')
            else: print('bad request')
        except:
            #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
            #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
            print("Skipping. Connnection error")
    
    return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)    

def get_proxies():
    proxies = []
    with open("http_proxies.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line.replace('\n',''))
    proxies = lines
    return proxies

def get_postalCodes():
    postalCodes = []
    with open("postalcodes.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line.replace('\n',''))
    postalCodes = lines
    return postalCodes

def getDistFromLatLon(lat1,lon1,lat2,lon2): #in km
  R = 6371 # Radius of the earth in km
  dLat = deg2rad(lat2-lat1)  # deg2rad below
  dLon = deg2rad(lon2-lon1)
  a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2) 
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)) 
  d = R * c # Distance in km
  return round(d,2)


def deg2rad(deg):
  return deg * (math.pi/180)

def populateDist(postalCode, codeList):
    lat_lon_list = parsePostal(postalCode)
    lat1 = lat_lon_list[0]
    lon1 = lat_lon_list[1]
    #i = 0
    print(codeList[1])
    distList = []
    for lat_lon in codeList[1]:
        print(lat_lon)
        distList.append(getDistFromLatLon(lat1, lon1, lat_lon[0], lat_lon[1]))
    print(distList)
    
    codeList.append(distList)
    return codeList

def show_requests(request):
    if(request.session['type'] == 'zoomer'):
        mylat, mylong = parsePostal(Zoomer.objects.get(pk=request.session['username']).postal_code)
        request_list=Requests.objects.filter(zoomer_id=request.session['username'])
        for request1 in request_list:
            dist = getDistFromLatLon(mylat,mylong,request1.boomer_id.latitude,request1.boomer_id.longitude)
            request1.boomer_id.distance = dist
            request1.boomer_id.save()
        
        context = {
            'request_list':request_list,
        }
        return render(request, 'nonboomer/taken_requests.html', context)
    elif(request.session['type'] == 'boomer'):
        mylat, mylong = parsePostal(Boomer.objects.get(pk=request.session['username']).postal_code)
        request_list=Requests.objects.filter(boomer_id=request.session['username'])
        myrequest_list = []
        for request1 in request_list:
            if(request1.zoomer_id == ''):
                myrequest_list.append({'id':request1.id, 'boomer_id': request1.boomer_id, 'zoomer_id':request1.zoomer_id, 'details':request1.details,'completed':request1.completed,'taken':request1.taken,'zoomer':''})
            else:
                zoomer = Zoomer.objects.get(pk=request1.zoomer_id)
                dist = getDistFromLatLon(mylat,mylong,zoomer.latitude,zoomer.longitude)
                myrequest_list.append({'id':request1.id, 'boomer_id': request1.boomer_id, 'zoomer_id':request1.zoomer_id, 'details':request1.details,'completed':request1.completed,'taken':request1.taken,'zoomer':zoomer, 'distance':dist})
        context = {
            'request_list':myrequest_list,
        }
        return render(request, 'boomer/myrequests.html', context)
    return render(request, 'login/index.html', {})

def requestComplete(request, id):
    request1 = Requests.objects.filter(id=id).first()
    request1.completed = True
    request1.save()
    return show_requests(request)

def accounts(request):
    zoomer=Zoomer.objects.get(pk=request.session['username'])
    context = {
        'zoomer': zoomer,
    }
    return render(request, 'nonboomer/editAccount.html', context)
def editZoomerConfirm(request):
    lat,longi  = parsePostal(request.POST['postalcode'])
    zoomer = Zoomer.objects.get(pk=request.session['username'])
    zoomer.username=request.POST['username']
    zoomer.password=request.POST['password']
    zoomer.name=request.POST['name']
    zoomer.surname=request.POST['surname']
    zoomer.email=request.POST['email']
    zoomer.postal_code=request.POST['postalcode']
    zoomer.address=request.POST['address']
    zoomer.age=request.POST['age']
    zoomer.phone=request.POST['phone']
    zoomer.latitude=lat
    zoomer.longitude=longi
    zoomer.save()
    context = {
        'zoomer': zoomer,
        'error_message':'Edit Successful'
    }
    return render(request, 'nonboomer/editAccount.html', context)