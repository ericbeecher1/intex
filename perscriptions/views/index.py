from django.conf import settings
from django_mako_plus import view_function, jscontext
from perscriptions import models as pmod
from django.contrib.auth.models import Permission

from django.contrib.auth.models import Group


@view_function
def process_request(request):

    context = {
    }
    return request.dmp.render('index.html', context)
