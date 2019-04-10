# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554920291.345091
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
        def main_content():
            return render_main_content(context._locals(__M_locals))
        int = context.get('int', UNDEFINED)
        self = context.get('self', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        round = context.get('round', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        def main_content():
            return render_main_content(context)
        int = context.get('int', UNDEFINED)
        self = context.get('self', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        round = context.get('round', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        __M_writer('            </h1>\n          </div>\n          <div class="col-12 col-lg-4">\n            <h3>Prescriber Details</h3>\n            <div class="well">\n              <div class="row p-2 border-bottom" style="border-bottom-style: dotted !important;">\n                <div class="col-4 text-right">\n                  Doctor ID:\n                </div>\n                <div class="col-8">\n                  ')
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
        __M_writer('\n                  </div>\n                </div>\n              </div>\n            </div>\n          </div>\n          <div class="col-12 col-lg-8">\n            <h3> Drugs Prescribed</h3>\n            <table class="datatable table table-striped table-bordered no-footer box-shadow">\n              <thead>\n                <tr>\n                <th class="nosort" style="width: 30px; text-align:center">\n\n                </th>\n                  <th>\n                    Name\n                  </th>\n                  <th class="text-center">\n                    Percentage of Perscriptions\n                  </th>\n                  <th class="text-center">\n                    # Prescribed\n                  </th>\n                  <th class="text-center">\n                    Average Prescribed\n                  </th>\n                </tr>\n\n              </thead>\n              <tbody>\n\n')
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
        __M_writer('              </tbody>\n            </table>\n          </div>\n        </div>\n      </div>\n    </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/perscriptions/templates/prescriber-view.html", "uri": "prescriber-view.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 133, "52": 3, "63": 3, "64": 9, "65": 10, "66": 10, "67": 10, "68": 10, "69": 10, "70": 11, "71": 12, "72": 12, "73": 12, "74": 14, "75": 24, "76": 24, "77": 27, "78": 28, "79": 33, "80": 33, "81": 33, "82": 33, "83": 37, "84": 42, "85": 42, "86": 50, "87": 50, "88": 58, "89": 58, "90": 66, "91": 66, "92": 73, "93": 73, "94": 104, "95": 105, "96": 107, "97": 108, "98": 108, "99": 108, "100": 110, "101": 113, "102": 113, "103": 113, "104": 113, "105": 116, "106": 116, "107": 119, "108": 119, "109": 122, "110": 122, "111": 127, "117": 111}}
__M_END_METADATA
"""
