# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554822594.376841
_enable_loop = True
_template_filename = '/Users/ericbeecher1/intex/perscriptions/templates/drugs.html'
_template_uri = 'drugs.html'
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
        drugs = context.get('drugs', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def main_content():
            return render_main_content(context._locals(__M_locals))
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
        drugs = context.get('drugs', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def main_content():
            return render_main_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <section>\n      <div class="container">\n        <div class="row">\n          <div class="col-12">\n            <h2 class="text-secondary pb-2">Drugs</h2>\n            <table class="datatable table table-striped table-bordered no-footer">\n              <thead>\n                <tr>\n                  <th class="nosort" style="width: 30px">\n\n                  </th>\n                  <th>\n                    Drug Name\n                  </th>\n                  <th class="nosort" style="text-align: center">\n                    Action\n                  </th>\n                </tr>\n\n              </thead>\n              <tbody>\n')
        for drug in drugs:
            __M_writer('                  <tr>\n                    <td class="text-center">\n')
            if drug.isOpioid:
                __M_writer('                        <i class="fas fa-capsules" data-toggle="tooltip" title="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.DrugName.capitalize()))
                __M_writer(' is an Opioid"></i>\n')
            __M_writer('                    </td>\n                    <td class="text-capitalize">\n                      <a href="/perscriptions/drugs.details/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.id))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.DrugName.lower()))
            __M_writer('</a>\n                    </td>\n                    <td class="actions_cell">\n                      <a href="/perscriptions/drugs.details/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.id))
            __M_writer('" class="btn btn-light btn-sm"><i class="fas fa-eye"></i></a>\n                    </td>\n                  </tr>\n\n')
        __M_writer('              </tbody>\n            </table>\n          </div>\n        </div>\n      </div>\n    </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/perscriptions/templates/drugs.html", "uri": "drugs.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 47, "49": 3, "57": 3, "58": 25, "59": 26, "60": 28, "61": 29, "62": 29, "63": 29, "64": 31, "65": 33, "66": 33, "67": 33, "68": 33, "69": 36, "70": 36, "71": 41, "77": 71}}
__M_END_METADATA
"""
