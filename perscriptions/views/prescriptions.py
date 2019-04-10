from django.conf import settings
from django_mako_plus import view_function, jscontext
from perscriptions import models as pmod
from django.http import HttpResponseRedirect




@view_function
def process_request(request):
    context = {
    }
    return request.dmp.render('prescribers.html', context)
@view_function
def add(request, prescriber:pmod.Prescriber=None):

    if request.method == 'POST':
        prescription = pmod.Prescriptions(Prescriber=prescriber)
        form = pmod.PrescriptionAddForm(request.POST, instance=prescription)
        drug = pmod.Drug.objects.get(pk=form.data['Drug'])
        try:
            duplicate_perscription = pmod.Prescriptions.objects.get(Drug=drug, Prescriber=prescriber)
        except pmod.Drug.DoesNotExist:
            if form.is_valid():
                form.save()
                # Update total
                prescriber = prescription.Prescriber
                prescriber.TotalPrescriptions = prescriber.TotalPrescriptions + int(form.data['QuanityPerscribed'])
                prescriber.save()
                request.session['message'] = '<div class="alert alert-success">That worked!</div>'
                return HttpResponseRedirect('/perscriptions/prescribers.edit/'+str(prescriber.id))
        else:
            request.session['message'] = '<div class="alert alert-warning">There is already an entry for that. Update it here</div>'
            return HttpResponseRedirect('/perscriptions/prescriptions.edit/'+str(duplicate_perscription.id))

    else:
        form = pmod.PrescriptionAddForm()

    context = {
        'prescriber': prescriber,
        'form': form,
    }
    return request.dmp.render('prescription-add.html', context)

@view_function
def delete(request, prescription:pmod.Prescriptions=None):
    if prescription is not None:
        prescription.delete()
        # Update total
        prescriber = prescription.Prescriber
        prescriber.TotalPrescriptions = prescriber.TotalPrescriptions - prescription.QuanityPerscribed
        prescriber.save()
        request.session['message'] = '<div class="alert alert-success">Prescription Deleted</div>'
    return HttpResponseRedirect('/perscriptions/prescribers.edit/'+str(prescriber.id))


@view_function
def edit(request, prescription:pmod.Prescriptions=None):


    try:
      request.session['message']
    except KeyError:
      message = ''
    else:
      message = request.session['message']
      request.session['message'] = ''
    if request.method == 'POST':

        og_quantity = prescription.QuanityPerscribed

        form = pmod.PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            # Update total
            prescriber = prescription.Prescriber
            prescriber.TotalPrescriptions = prescriber.TotalPrescriptions - og_quantity + int(form.data['QuanityPerscribed'])
            prescriber.save()
            request.session['message'] = '<div class="alert alert-success">Prescription Updated!</div>'
            return HttpResponseRedirect('/perscriptions/prescribers.edit/'+str(prescriber.id))


    else:
        form = pmod.PrescriptionForm(instance=prescription)

    context = {
        'prescription': prescription,
        'form': form,
        'message': message
    }
    return request.dmp.render('prescription-edit.html', context)
