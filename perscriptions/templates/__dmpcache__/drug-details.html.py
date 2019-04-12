# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555026544.630837
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
        set = context.get('set', UNDEFINED)
        def main_content():
            return render_main_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        drug = context.get('drug', UNDEFINED)
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
        set = context.get('set', UNDEFINED)
        def main_content():
            return render_main_content(context)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        drug = context.get('drug', UNDEFINED)
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
        __M_writer('              </tbody>\n            </table>\n          </div>\n')
        if drug.isOpioid :
            __M_writer('          <div class="col-12">\n            ')

            if drug.isOpioid :
                similar_drugs = drug.get_similar_drugs()
            else:
                similar_drugs = set()
            
            
            __M_writer('\n\n            <h3>Similar Drugs</h3>\n            <table class="datatable table table-striped table-bordered no-footer">\n              <thead>\n                <tr>\n                  <th class="nosort" style="width: 30px">\n\n                  </th>\n                  <th>\n                    Drug Name\n                  </th>\n                  <th class="nosort" style="text-align: center">\n                    Action\n                  </th>\n                </tr>\n\n              </thead>\n              <tbody>\n')
            for similar_drug in similar_drugs:
                __M_writer('                  <tr>\n                    <td class="text-center">\n')
                if similar_drug.isOpioid:
                    __M_writer('                        <i class="fas fa-capsules" data-toggle="tooltip" title="')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_drug.DrugName.capitalize()))
                    __M_writer(' is an Opioid"></i>\n')
                __M_writer('                    </td>\n                    <td class="text-capitalize">\n                      <a href="/perscriptions/drugs.details/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_drug.id))
                __M_writer('">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_drug.DrugName.lower()))
                __M_writer('</a>\n                    </td>\n                    <td class="actions_cell">\n                      <a href="/perscriptions/drugs.details/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(similar_drug.id))
                __M_writer('" class="btn btn-light btn-sm"><i class="fas fa-eye"></i></a>\n                    </td>\n                  </tr>\n\n')
            __M_writer('              </tbody>\n            </table>\n          </div>\n')
        __M_writer('\n        </div>\n      </div>\n    </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/perscriptions/templates/drug-details.html", "uri": "drug-details.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 137, "51": 3, "61": 3, "62": 8, "63": 8, "64": 18, "65": 18, "66": 26, "67": 27, "68": 28, "69": 29, "70": 31, "71": 36, "72": 36, "73": 43, "74": 44, "75": 47, "76": 48, "77": 52, "78": 62, "79": 63, "80": 65, "81": 65, "82": 68, "83": 69, "84": 69, "85": 69, "86": 69, "87": 69, "88": 69, "89": 69, "90": 70, "91": 71, "92": 71, "93": 71, "94": 71, "95": 71, "96": 73, "97": 76, "98": 76, "99": 79, "100": 79, "101": 84, "102": 87, "103": 88, "104": 89, "111": 94, "112": 113, "113": 114, "114": 116, "115": 117, "116": 117, "117": 117, "118": 119, "119": 121, "120": 121, "121": 121, "122": 121, "123": 124, "124": 124, "125": 129, "126": 133, "132": 126}}
__M_END_METADATA
"""
