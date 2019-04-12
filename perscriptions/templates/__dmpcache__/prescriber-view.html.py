# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555015376.265135
_enable_loop = True
_template_filename = '/Users/ericbeecher1/intex/perscriptions/templates/prescriber-view.html'
_template_uri = 'prescriber-view.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['main_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        prescriber = context.get('prescriber', UNDEFINED)
        def main_content():
            return render_main_content(context._locals(__M_locals))
        round = context.get('round', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        similar_prescribers = context.get('similar_prescribers', UNDEFINED)
        int = context.get('int', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_content'):
            context['self'].main_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        prescriber = context.get('prescriber', UNDEFINED)
        def main_content():
            return render_main_content(context)
        round = context.get('round', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        similar_prescribers = context.get('similar_prescribers', UNDEFINED)
        int = context.get('int', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <section>\n      <div class="container">\n        <div class="row">\n          <div class="col-12">\n            <h1 class="border-bottom mb-4 pb-1" style="border-bottom-style: dotted!important;">\n')
        if request.user.has_perm('perscriptions.can_see_names') :
            __M_writer('                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Fname))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Lname))
            __M_writer('\n')
        else:
            __M_writer('                Prescriber #')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.DoctorID))
            __M_writer('\n')
        __M_writer('            </h1>\n          </div>\n\n            <div class="col-12">\n')
        if prescriber.get_high_risk():
            __M_writer('              <div class="alert alert-danger">\n                This Prescriber has a higher opioid prescription rate than comparable prescribers\n              </div>\n')
        else:
            __M_writer('              <div class="alert alert-success">\n                This Prescriber has a lower opioid prescription rate than comparable prescribers\n              </div>\n')
        __M_writer('            </div>\n\n\n          <div class="col-12 col-lg-4">\n            <h3>Prescriber Details</h3>\n            <div class="well">\n              <div class="row p-2 border-bottom" style="border-bottom-style: dotted !important;">\n                <div class="col-4 text-right">\n                  Doctor ID:\n                </div>\n                <div class="col-8">\n                  ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.DoctorID))
        __M_writer('\n                </div>\n              </div>\n')
        if request.user.has_perm('perscriptions.can_see_names') :
            __M_writer('                <div class="row p-2 border-bottom" style="border-bottom-style: dotted !important;">\n                  <div class="col-4 text-right">\n                    Name:\n                  </div>\n                  <div class="col-8">\n                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Fname))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Lname))
            __M_writer('\n                  </div>\n                </div>\n')
        __M_writer('              <div class="row p-2 border-bottom" style="border-bottom-style: dotted !important;">\n                <div class="col-4 text-right">\n                  Gender:\n                </div>\n                <div class="col-8">\n                  ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Gender))
        __M_writer('\n                </div>\n              </div>\n              <div class="row p-2 border-bottom" style="border-bottom-style: dotted !important;">\n                <div class="col-4 text-right">\n                  Location:\n                </div>\n                <div class="col-8">\n                  ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.State))
        __M_writer('\n                </div>\n              </div>\n              <div class="row p-2 border-bottom" style="border-bottom-style: dotted !important;">\n                <div class="col-4 text-right">\n                  Credentials:\n                </div>\n                <div class="col-8">\n                  ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Credentials))
        __M_writer('\n                </div>\n              </div>\n              <div class="row p-2 border-bottom" style="border-bottom-style: dotted !important;">\n                <div class="col-4 text-right">\n                  Specialty:\n                </div>\n                <div class="col-8">\n                  ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Specialty))
        __M_writer('\n                </div>\n                <div class="row p-2">\n                  <div class="col-6 text-right">\n                    Total Prescriptions:\n                  </div>\n                  <div class="col-6 align-self-center">\n                    ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.TotalPrescriptions))
        __M_writer('\n                  </div>\n                </div>\n              </div>\n            </div>\n\n\n          </div>\n          <div class="col-12 col-lg-8">\n            <h3> Drugs Prescribed</h3>\n            <table class="table table-striped table-bordered no-footer box-shadow">\n              <thead>\n                <tr>\n                <th class="nosort" style="width: 30px; text-align:center">\n\n                </th>\n                  <th>\n                    Name\n                  </th>\n                  <th class="text-center">\n                    Percentage of Perscriptions\n                  </th>\n                  <th class="text-center">\n                    # Prescribed\n                  </th>\n                  <th class="text-center">\n                    Average Prescribed\n                  </th>\n                </tr>\n\n              </thead>\n              <tbody>\n\n')
        for prescription in prescriber.get_drugs_perscribed():
            __M_writer('                  <tr>\n                    <td class="text-center">\n')
            if prescription.Drug.isOpioid:
                __M_writer('                        <i class="fas fa-capsules" data-toggle="tooltip" title="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Drug.DrugName.capitalize()))
                __M_writer(' is an Opioid"></i>\n')
            __M_writer('                    </td>\n                    </td>\n                    <td>\n                      <a href="/perscriptions/drugs.details/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Drug.id))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Drug.DrugName.capitalize()))
            __M_writer('</a>\n                    </td>\n                    <td class="text-center">\n                      ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(round(prescription.QuanityPerscribed / int(prescriber.TotalPrescriptions)* 100, 1) ))
            __M_writer('%\n                    </td>\n                    <td class="text-center">\n                      ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.QuanityPerscribed))
            __M_writer('\n                    </td>\n                    <td class="text-center">\n                      ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Drug.get_average_perscribed()))
            __M_writer('\n                    </td>\n                  </tr>\n\n')
        __M_writer('              </tbody>\n            </table>\n            <h3> Similar Doctors</h3>\n            <table class="datatable table table-striped table-bordered no-footer">\n              <thead>\n                <tr>\n                  <th class="nosort" style="width: 30px">\n\n                  </th>\n')
        if request.user.has_perm('perscriptions.can_see_names') :
            __M_writer('                    <th>\n                      Name\n                    </th>\n')
        else:
            __M_writer('                    <th>\n                      Doctor ID\n                    </th>\n')
        __M_writer('                  <th>\n                    Location\n                  </th>\n                  <th>\n                    Credentials\n                  </th>\n                  <th>\n                    Specialty\n                  </th>\n\n                  <th class="nosort" style="text-align: center">\n                    Actions\n                  </th>\n                </tr>\n\n              </thead>\n              <tbody>\n')
        for similar_prescriber in similar_prescribers:
            __M_writer('                  <tr>\n                    <td class="text-center">\n\n                    </td>\n')
            if request.user.has_perm('perscriptions.can_see_names') :
                __M_writer('                      <td>\n                        <a href="/perscriptions/prescribers.view/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_prescriber.id))
                __M_writer('">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_prescriber.Fname))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_prescriber.Lname))
                __M_writer('</a>\n                      </td>\n')
            else:
                __M_writer('                      <td>\n                        <a href="/perscriptions/prescribers.view/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_prescriber.id))
                __M_writer('">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_prescriber.DoctorID))
                __M_writer('</a>\n                      </td>\n')
            __M_writer('                    <td>\n                      ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_prescriber.State))
            __M_writer('</a>\n                    </td>\n                    <td>\n                      ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_prescriber.Credentials))
            __M_writer('</a>\n                    </td>\n                    <td>\n                      ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_prescriber.Specialty))
            __M_writer('</a>\n                    </td>\n                    <td class="text-center">\n                      <a href="/perscriptions/prescribers.view/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_prescriber.id))
            __M_writer('" class="btn btn-light btn-sm"><i class="fas fa-eye"></i></a>\n')
            if request.user.has_perm('perscriptions.can_crud') :
                __M_writer('                        <a href="/perscriptions/prescribers.edit/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_prescriber.id))
                __M_writer('" class="btn btn-success btn-sm"><i class="fas fa-edit"></i></a>\n                        <a href="/perscriptions/prescribers.delete/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_prescriber.id))
                __M_writer('" onclick="confirm(\'Are you sure? This cannot be undone\')" class="btn btn-danger btn-sm"><i class="fas fa-trash"></i></a>\n')
            __M_writer('                    </td>\n                  </tr>\n\n')
        __M_writer('              </tbody>\n            </table>\n          </div>\n\n        </div>\n      </div>\n    </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/perscriptions/templates/prescriber-view.html", "uri": "prescriber-view.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 218, "53": 3, "65": 3, "66": 9, "67": 10, "68": 10, "69": 10, "70": 10, "71": 10, "72": 11, "73": 12, "74": 12, "75": 12, "76": 14, "77": 18, "78": 19, "79": 22, "80": 23, "81": 27, "82": 38, "83": 38, "84": 41, "85": 42, "86": 47, "87": 47, "88": 47, "89": 47, "90": 51, "91": 56, "92": 56, "93": 64, "94": 64, "95": 72, "96": 72, "97": 80, "98": 80, "99": 87, "100": 87, "101": 120, "102": 121, "103": 123, "104": 124, "105": 124, "106": 124, "107": 126, "108": 129, "109": 129, "110": 129, "111": 129, "112": 132, "113": 132, "114": 135, "115": 135, "116": 138, "117": 138, "118": 143, "119": 152, "120": 153, "121": 156, "122": 157, "123": 161, "124": 178, "125": 179, "126": 183, "127": 184, "128": 185, "129": 185, "130": 185, "131": 185, "132": 185, "133": 185, "134": 187, "135": 188, "136": 189, "137": 189, "138": 189, "139": 189, "140": 192, "141": 193, "142": 193, "143": 196, "144": 196, "145": 199, "146": 199, "147": 202, "148": 202, "149": 203, "150": 204, "151": 204, "152": 204, "153": 205, "154": 205, "155": 207, "156": 211, "162": 156}}
__M_END_METADATA
"""
