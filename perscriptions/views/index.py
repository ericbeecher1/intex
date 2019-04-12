from django.conf import settings
from django_mako_plus import view_function, jscontext
from perscriptions import models as pmod
from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from perscriptions import models as pmod
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/')
@view_function
def process_request(request):
    if request.user.has_perm('perscriptions.can_crud') :
        return HttpResponseRedirect('/perscriptions/drugs/')
    else:
        if request.user.has_perm('perscriptions.can_see_names'):
            prescriber = False
            health_offical = True
        else :
            prescriber = True
            health_offical = False
        context = {
            'prescriber': prescriber,
            'health_offical': health_offical
        }
        return request.dmp.render('index.html', context)
