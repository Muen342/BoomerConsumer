from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from ..models import Boomer, Requests
from django.views import generic
from django.db import connection
import datetime

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def listing(request):
    boomer_list = Boomer.objects.all()
    myboomer_list = []
    for boomer in boomer_list:
        request_list = Requests.objects.filter(boomer_id=boomer.username)
        newBoomer = {'name':boomer.name, 'surname':boomer.surname, 'age':boomer.age, 'postal_code':boomer.postal_code, 'request_list': request_list}
        myboomer_list.append(newBoomer)
    context = {
        'boomer_list': myboomer_list,
    }
    request.session['username'] = 'mzhang'
    request.session['type'] = 'zoomer'
    return render(request, 'nonboomer/listing.html', context)

def requestTake(request, id):
    request1 = Requests.objects.filter(id=id).first()
    request1.taken = True
    request1.save()
    #save the zoomer that took it too, but we need the zoomer id in session storage to access (get during login)
    boomer_list = Boomer.objects.all()
    myboomer_list = []
    for boomer in boomer_list:
        request_list = Requests.objects.filter(boomer_id=boomer.username)
        newBoomer = {'name':boomer.name, 'surname':boomer.surname, 'age':boomer.age, 'postal_code':boomer.postal_code, 'request_list': request_list}
        myboomer_list.append(newBoomer)
    context = {
        'boomer_list': myboomer_list,
    }
    return render(request, 'nonboomer/listing.html', context)