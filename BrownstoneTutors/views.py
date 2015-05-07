from allauth.account.views import *

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, Template , Context

def index(request):
    return render_to_response('index.html', RequestContext(request))
