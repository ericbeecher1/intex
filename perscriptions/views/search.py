from django.conf import settings
from django_mako_plus import view_function, jscontext
from perscriptions import models as pmod
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/')
@view_function
def process_request(request):
    if request.method == 'POST':
        search_term = request.POST.dict().get('search_term')
        drug_results = pmod.Drug.objects.filter(DrugName__icontains=search_term)
        p_gender_results = pmod.Prescriber.objects.filter(Gender__icontains=search_term)
        p_id_results = pmod.Prescriber.objects.filter(DoctorID__icontains=search_term)
        p_specialty_results = pmod.Prescriber.objects.filter(Specialty__icontains=search_term)
        p_total_results = pmod.Prescriber.objects.filter(TotalPrescriptions__icontains=search_term)

        if request.user.has_perm('perscriptions.can_see_names') :
            p_fname_results = pmod.Prescriber.objects.filter(Fname__icontains=search_term)
            p_lname_results  = pmod.Prescriber.objects.filter(Lname__icontains=search_term)
            prescriber_results = p_gender_results | p_id_results | p_specialty_results | p_total_results | p_fname_results | p_lname_results
        else:
            prescriber_results = p_gender_results | p_id_results | p_specialty_results | p_total_results

        prescriber_results = prescriber_results.distinct()


    else:
        drug_results = set()
        prescriber_results = set()
        search_term = ''


    context = {
        'drug_results': drug_results,
        'prescriber_results': prescriber_results,
        'search_term': search_term
    }




    return request.dmp.render('search.html', context)
