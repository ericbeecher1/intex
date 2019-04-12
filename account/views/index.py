from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from account import models as amod
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt



@view_function
def process_request(request):

    class NameForm(forms.Form):
        username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': "form-control"}))
        password = forms.CharField(label = "Password", widget=forms.PasswordInput(attrs={'class': "form-control"}))

    if request.user.is_authenticated :
        if request.user.has_perm('perscriptions.can_crud') :
            return HttpResponseRedirect('/perscriptions/drugs')
        else:
            return HttpResponseRedirect('/perscriptions/')
    else:

        if request.method == 'POST':
            form = NameForm(request.POST)


            if form.is_valid():
                user = authenticate(username=form.data['username'], password=form.data['password'])
                # Login
                if user is not None:
                    login(request, user);
                    request.session['message'] = ''

                    try:
                        request.GET.dict().get('next')
                    except:
                        if user.has_perm('perscriptions.can_crud') :
                            return HttpResponseRedirect('/perscriptions/drugs/')
                        else :
                            return HttpResponseRedirect('/perscriptions/')
                    else :
                        return HttpResponseRedirect(request.GET.dict().get('next'))



        else:
            form = NameForm()

        context = {
            'form': form
        }
        return request.dmp.render('index.html', context)
