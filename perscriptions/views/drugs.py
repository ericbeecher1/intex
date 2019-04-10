from django.conf import settings
from django_mako_plus import view_function, jscontext
import csv
from perscriptions import models as pmod





@view_function
def process_request(request):
    drugs = pmod.Drug.objects.all()

    context = {
        'drugs': drugs
    }
    return request.dmp.render('drugs.html', context)

@view_function
def details(request, drug:pmod.Drug=None):
    context = {
        'drug': drug
    }
    return request.dmp.render('drug-details.html', context)
