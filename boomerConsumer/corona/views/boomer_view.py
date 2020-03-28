from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from ..models import Boomer
from django.views import generic
from django.db import connection
import datetime


def listing(request):
    boomer_list = Boomer.objects.all()
    template = loader.get_template('boomer/listing.html')
    context = {
        'boomer_list': boomer_list,
    }
    return HttpResponse(template.render(context, request))