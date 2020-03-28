from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from ..models import Boomer, Requests
from django.views import generic
from django.db import connection
import datetime


def listing(request):
    boomer_list = Boomer.objects.all()
    # myboomer_list = []
    # for boomer in boomer_list:
    #     requests = boomer.requests[1:-1].split('*,*')
    #     request_list = []
    #     for request in requests:
    #         tempreq = Requests.objects.get(pk=1)
            # request_list.append(tempreq)
    #     newBoomer = {'name':boomer.name, 'surname':boomer.surname, 'age':boomer.age, 'postal_code':boomer.postal_code, 'request_list': request_list}
    #     myboomer_list.append(newBoomer)
    
    template = loader.get_template('boomer/listing.html')
    context = {
        'boomer_list': boomer_list,
    }
    return render(request, 'boomer/listing.html', context)