# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554920327.583138
_enable_loop = True
_template_filename = '/Users/ericbeecher1/intex/perscriptions/templates/drug-details.html'
_template_uri = 'drug-details.html'
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
        self = context.get('self', UNDEFINED)
        def main_content():
            return render_main_content(context._locals(__M_locals))
        drug = context.get('drug', UNDEFINED)
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
        self = context.get('self', UNDEFINED)
        def main_content():
            return render_main_content(context)
        drug = context.get('drug', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <section>\n      <div class="container">\n        <div class="row">\n          <div class="col-12">\n            <h1 class="border-bottom mb-4 pb-1" style="border-bottom-style: dotted!important;">  ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.DrugName.capitalize()))
        __M_writer('</h1>\n          </div>\n          <div class="col-12 col-lg-4">\n            <h3>Drug Details</h3>\n            <div class="well">\n              <div class="row p-2 border-bottom" style="border-bottom-style: dotted !important;">\n                <div class="col-4 text-right">\n                  Name:\n                </div>\n                <div class="col-8">\n                  ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.DrugName.capitalize()))
        __M_writer('\n                </div>\n              </div>\n              <div class="row p-2">\n                <div class="col-4 text-right">\n                  Is Opioid:\n                </div>\n                <div class="col-8">\n')
        if drug.isOpioid:
            __M_writer('                    Yes\n')
        else:
            __M_writer('                    No\n')
        __M_writer('                </div>\n              </div>\n            </div>\n          </div>\n          <div class="col-12 col-lg-8">\n            <h3>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.DrugName.capitalize()))
        __M_writer(' Top Prescribers</h3>\n            <table class="datatable table table-striped table-bordered no-footer box-shadow">\n              <thead>\n                <tr>\n                  <th class="nosort" style="width: 30px; text-align:center">\n                    # Prescribed\n                  </th>\n')
        if request.user.has_perm('perscriptions.can_see_names') :
            __M_writer('                    <th>\n                      Name\n                    </th>\n')
        else:
            __M_writer('                    <th>\n                      Doctor Id\n                    </th>\n')
        __M_writer('                  <th>\n                    Location\n                  </th>\n                  <th>\n                    Specialty\n                  </th>\n                </tr>\n\n              </thead>\n              <tbody>\n')
        for prescription in drug.get_top_prescriptions():
            __M_writer('                  <tr>\n                    <td class="text-center">\n                      ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.QuanityPerscribed))
            __M_writer('\n                    </td>\n                    <td class="text-capitalize">\n')
            if request.user.has_perm('perscriptions.can_see_names') :
                __M_writer('                      <a href="/perscriptions/prescribers.view/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Prescriber.id))
                __M_writer('">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Prescriber.Fname))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Prescriber.Lname))
                __M_writer('</a>\n')
            else:
                __M_writer('                      <a href="/perscriptions/prescribers.view/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Prescriber.id))
                __M_writer('">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Prescriber.DoctorID))
                __M_writer('</a>\n')
            __M_writer('                    </td>\n\n                    <td>\n                      ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Prescriber.State))
            __M_writer('\n                    </td>\n                    <td>\n                      ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Prescriber.Specialty))
            __M_writer('\n                    </td>\n                  </tr>\n\n')
        __M_writer('              </tbody>\n            </table>\n          </div>\n        </div>\n      </div>\n    </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/perscriptions/templates/drug-details.html", "uri": "drug-details.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "44": 90, "50": 3, "59": 3, "60": 8, "61": 8, "62": 18, "63": 18, "64": 26, "65": 27, "66": 28, "67": 29, "68": 31, "69": 36, "70": 36, "71": 43, "72": 44, "73": 47, "74": 48, "75": 52, "76": 62, "77": 63, "78": 65, "79": 65, "80": 68, "81": 69, "82": 69, "83": 69, "84": 69, "85": 69, "86": 69, "87": 69, "88": 70, "89": 71, "90": 71, "91": 71, "92": 71, "93": 71, "94": 73, "95": 76, "96": 76, "97": 79, "98": 79, "99": 84, "105": 99}}
__M_END_METADATA
"""
