from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from account import models as amod
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login


@view_function
def process_request(request):
    logout(request)
    return HttpResponseRedirect('/account/')
    
