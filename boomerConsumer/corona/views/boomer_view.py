from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from ..models import Boomer, Requests
from django.views import generic
from django.db import connection
import datetime
from .nonboomer_view import show_requests

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
        newBoomer = {'name':boomer.name, 'surname':boomer.surname, 'age':boomer.age, 'postal_code':boomer.postal_code, 'email':boomer.email, 'phone': boomer.phone, 'address':boomer.address, 'request_list': request_list}
        myboomer_list.append(newBoomer)
    context = {
        'boomer_list': myboomer_list,
    }
    return render(request, 'nonboomer/listing.html', context)

def requestTake(request, id):
    request1 = Requests.objects.filter(id=id).first()
    request1.zoomer_id = 'mzhang'
    request1.taken = True
    request1.save()
    #save the zoomer that took it too, but we need the zoomer id in session storage to access (get during login)
    return listing(request)

def add(request):
    return render(request, 'boomer/add.html', {})

def addListing(request):
    if(request.POST['details'] == ''):
        return render(request, 'boomer/add.html', {'error_message': 'Enter some details'})
    else:
        r = Requests(boomer_id=Boomer.objects.get(pk=request.session['username']), details=request.POST['details'])
        r.save()
        return render(request, 'boomer/add.html', {'error_message': 'Successfully added'})



def editListing(request, id):
    request1 = Requests.objects.get(pk=id)
    context = {
        'request1': request1
    }
    return render(request, 'boomer/editRequest.html', context)

def confirmEditListing(request, id):
    request1 = Requests.objects.get(pk=id)
    if(request.POST['details'] == ''):
        return render(request, 'boomer/editRequest.html', {'request1': request1,'error_message':'Enter the details of the request'})
    request1.details = request.POST['details']
    request1.save()
    context = {
        'request1': request1,
        'error_message':'Successfully edited',
    }
    return render(request, 'boomer/editRequest.html', context)

def deleteListing(request, id):
    request1 = Requests.objects.get(pk=id)
    request1.delete()
    return show_requests(request)