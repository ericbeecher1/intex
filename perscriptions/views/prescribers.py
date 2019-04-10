from django.conf import settings
from django_mako_plus import view_function, jscontext
from perscriptions import models as pmod
from django.http import HttpResponseRedirect




@view_function
def process_request(request, page:int=1):
    page_length = 10
    total = pmod.Prescriber.objects.all().count()
    # account for remainder
    remainder = total % page_length
    if remainder == 0:
        num_of_pages = total/page_length
    else:
        num_of_pages = ((total - remainder)/page_length) + 1

    # Message
    try:
      request.session['message']
    except KeyError:
      message = ''
    else:
      message = request.session['message']
      request.session['message'] = ''

    up_and_down = 2

    # Pagination
    if page > up_and_down + up_and_down:
        dot_down = '<li class="paginate_button page-item disabled"><a href="/perscriptions/prescribers/" aria-controls="DataTables_Table_0" data-dt-idx="6" tabindex="0" class="page-link">…</a></li>'
    else:
        dot_down = ''

    if num_of_pages - page > up_and_down + 1:
        dot_up = '<li class="paginate_button page-item disabled"><a href="/perscriptions/prescribers/" aria-controls="DataTables_Table_0" data-dt-idx="6" tabindex="0" class="page-link">…</a></li>'
    else:
        dot_up = ''

    if page > up_and_down+1 :
        first_page = '<li class="paginate_button page-item "><a href="/perscriptions/prescribers/1" tabindex="0" class="page-link">1</a></li>'
    else :
        first_page = ''

    if num_of_pages - page > up_and_down :
        last_page = '<li class="paginate_button page-item "><a href="/perscriptions/prescribers/'+str(int(num_of_pages))+'" tabindex="0" class="page-link">'+str(int(num_of_pages))+'</a></li>'
    else :
        last_page = ''

    if page - 1 < up_and_down :
        down_pages = page - 1
        up_pages = int((up_and_down * 2) - down_pages)
    elif page + 1 > (num_of_pages -1):
        up_pages = int(num_of_pages - page)
        down_pages = int((up_and_down * 2) - up_pages)
    else :
        up_pages = up_and_down
        down_pages = up_and_down

    print(up_pages)

    if page > 1:
        prev = ''
    else:
        prev = 'disabled'

    if page < num_of_pages:
        next = ''
    else:
        next = 'disabled'

    pagination = '<li class="paginate_button page-item previous '+prev+'"><a href="/perscriptions/prescribers/'+str(page-1)+'" class="page-link">Previous</a></li>' + first_page + dot_down

    # Down pagination
    for page_num in range(down_pages):
        pagination += '<li class="paginate_button page-item "><a href="/perscriptions/prescribers/'+str(page-down_pages + page_num)+'" tabindex="0" class="page-link">'+str(page-down_pages + page_num)+'</a></li>'
    # Current Page
    pagination += '<li class="paginate_button page-item active"><a href="javascript:void(0)" tabindex="0" class="page-link">'+str(page)+'</a></li>'
    # Up Pagination
    for page_num in range(up_pages):
        pagination += '<li class="paginate_button page-item "><a href="/perscriptions/prescribers/'+str(page+page_num+1)+'" tabindex="0" class="page-link">'+str(page+page_num+1)+'</a></li>'

    pagination += dot_up + last_page + '<li class="paginate_button page-item '+next+'"><a href="/perscriptions/prescribers/'+str(page+1)+'" class="page-link">Next</a></li>'
    # Presribers
    prescribers = pmod.Prescriber.objects.all().order_by('DoctorID')[((page-1)*page_length): (page*page_length)]

    if page == num_of_pages:
        end = total
    else:
        end = page*page_length
    context = {
        'prescribers': prescribers,
        'pagination': pagination,
        'start': ((page-1)*page_length) + 1,
        'end': end,
        'total': int(total),
        'message': message
    }
    return request.dmp.render('prescribers.html', context)

@view_function
def view(request, prescriber:pmod.Prescriber=None):
    context = {
        'prescriber': prescriber
    }
    return request.dmp.render('prescriber-view.html', context)


@view_function
def edit(request, prescriber:pmod.Prescriber=None):

    try:
      request.session['message']
    except KeyError:
      message = ''
    else:
      message = request.session['message']
      request.session['message'] = ''

    if request.method == 'POST':
        form = pmod.PrescriberForm(request.POST, instance=prescriber)
        if form.is_valid():
            form.save()
            request.session['message'] = '<div class="alert alert-success">That worked!</div>'
            return HttpResponseRedirect('/perscriptions/prescribers.edit/'+str(prescriber.id))


    else:
        form = pmod.PrescriberForm(instance=prescriber)

    context = {
        'prescriber': prescriber,
        'form': form,
        'message': message
    }
    return request.dmp.render('prescriber-edit.html', context)

@view_function
def add(request):

    if request.method == 'POST':
        form = pmod.PrescriberForm(request.POST)
        if form.is_valid():
            form.save()
            page_length = 10
            total = pmod.Prescriber.objects.all().count()
            remainder = total % page_length
            if remainder == 0:
                num_of_pages = total/page_length
            else:
                num_of_pages = ((total - remainder)/page_length) + 1
            request.session['message'] = '<div class="alert alert-success">Look at your new Prescriber!</div>'
            return HttpResponseRedirect('/perscriptions/prescribers/'+str(round(num_of_pages)))


    else:
        form = pmod.PrescriberForm()

    context = {
        'form': form,
    }
    return request.dmp.render('prescriber-add.html', context)
@view_function
def delete(request, prescriber:pmod.Prescriber=None):

    if prescriber is not None:
        prescriber.delete()
        request.session['message'] = '<div class="alert alert-success">Prescriber Deleted</div>'

    return HttpResponseRedirect('/perscriptions/prescribers')
