from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from ..models import Boomer, Requests
from django.urls import reverse
from django.views import generic
from django.db import connection
import datetime

def show_requests(request):
    if(request.session['type'] == 'zoomer'):
        request_list=Requests.objects.filter(zoomer_id=request.session['username'])
        context = {
            'request_list':request_list,
        }
        return render(request, 'nonboomer/taken_requests.html', context)
    elif(request.session['type'] == 'boomer'):
        request_list=Requests.objects.filter(boomer_id=request.session['username'])
        context = {
            'request_list':request_list,
        }
        return render(request, 'nonboomer/myrequests.html', context)
    return render(request, 'login/index.html', {})

def requestComplete(request, id):
    request1 = Requests.objects.filter(id=id).first()
    request1.completed = True
    request1.save()
    return show_requests(request)