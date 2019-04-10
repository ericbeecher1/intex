# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554919356.7113369
_enable_loop = True
_template_filename = '/Users/ericbeecher1/intex/perscriptions/templates/prescribers.html'
_template_uri = 'prescribers.html'
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
        end = context.get('end', UNDEFINED)
        self = context.get('self', UNDEFINED)
        pagination = context.get('pagination', UNDEFINED)
        def main_content():
            return render_main_content(context._locals(__M_locals))
        total = context.get('total', UNDEFINED)
        start = context.get('start', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        request = context.get('request', UNDEFINED)
        message = context.get('message', UNDEFINED)
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
        end = context.get('end', UNDEFINED)
        self = context.get('self', UNDEFINED)
        pagination = context.get('pagination', UNDEFINED)
        def main_content():
            return render_main_content(context)
        total = context.get('total', UNDEFINED)
        start = context.get('start', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        request = context.get('request', UNDEFINED)
        message = context.get('message', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <section>\n      <div class="container">\n        <div class="row">\n          <div class="col-12">\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self, extra={'n_filter_on': True})(message ))
        __M_writer('\n            <h2 class="text-secondary pb-2">Prescribers</h2>\n            <div class="dataTables_wrapper">\n\n              <table class="datatable table table-striped table-bordered no-footer">\n                <thead>\n                  <tr>\n                    <th class="nosort" style="width: 30px">\n\n                    </th>\n')
        if request.user.has_perm('perscriptions.can_see_names') :
            __M_writer('                      <th>\n                        Name\n                      </th>\n')
        else:
            __M_writer('                      <th>\n                        Doctor ID\n                      </th>\n')
        __M_writer('                    <th>\n                      Location\n                    </th>\n                    <th>\n                      Credentials\n                    </th>\n                    <th>\n                      Specialty\n                    </th>\n\n                    <th class="nosort" style="text-align: center">\n                      Actions\n                    </th>\n                  </tr>\n\n                </thead>\n                <tbody>\n')
        for prescriber in prescribers:
            __M_writer('                    <tr>\n                      <td class="text-center">\n\n                      </td>\n')
            if request.user.has_perm('perscriptions.can_see_names') :
                __M_writer('                        <td>\n                          <a href="/perscriptions/prescribers.view/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.id))
                __M_writer('">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Fname))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Lname))
                __M_writer('</a>\n                        </td>\n')
            else:
                __M_writer('                        <td>\n                          <a href="/perscriptions/prescribers.view/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.id))
                __M_writer('">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.DoctorID))
                __M_writer('</a>\n                        </td>\n')
            __M_writer('                      <td>\n                        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.State))
            __M_writer('</a>\n                      </td>\n                      <td>\n                        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Credentials))
            __M_writer('</a>\n                      </td>\n                      <td>\n                        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Specialty))
            __M_writer('</a>\n                      </td>\n                      <td class="text-center">\n                        <a href="/perscriptions/prescribers.view/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.id))
            __M_writer('" class="btn btn-light btn-sm"><i class="fas fa-eye"></i></a>\n')
            if request.user.has_perm('perscriptions.can_crud') :
                __M_writer('                          <a href="/perscriptions/prescribers.edit/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.id))
                __M_writer('" class="btn btn-success btn-sm"><i class="fas fa-edit"></i></a>\n                          <a href="/perscriptions/prescribers.delete/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.id))
                __M_writer('" onclick="confirm(\'Are you sure? This cannot be undone\')" class="btn btn-danger btn-sm"><i class="fas fa-trash"></i></a>\n')
            __M_writer('                      </td>\n                    </tr>\n\n')
        __M_writer('                </tbody>\n              </table>\n              <div class="row">\n                <div class="col-sm-12 col-md-5">\n                  <div class="dataTables_info" id="DataTables_Table_0_info" role="status" aria-live="polite">Showing ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(start))
        __M_writer(' to ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(end))
        __M_writer(' of ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(total))
        __M_writer(' entries</div>\n                </div>\n                <div class="col-sm-12 col-md-7">\n                  <div class="dataTables_paginate paging_simple_numbers" id="DataTables_Table_0_paginate">\n                    <ul class="pagination">\n                      ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self, extra={'n_filter_on': True})(pagination ))
        __M_writer('\n                      </ul>\n                    </div>\n                  </div>\n              </div>\n            </div>\n          </div>\n\n        </div>\n      </div>\n    </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/perscriptions/templates/prescribers.html", "uri": "prescribers.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 97, "55": 3, "69": 3, "70": 8, "71": 8, "72": 18, "73": 19, "74": 22, "75": 23, "76": 27, "77": 44, "78": 45, "79": 49, "80": 50, "81": 51, "82": 51, "83": 51, "84": 51, "85": 51, "86": 51, "87": 53, "88": 54, "89": 55, "90": 55, "91": 55, "92": 55, "93": 58, "94": 59, "95": 59, "96": 62, "97": 62, "98": 65, "99": 65, "100": 68, "101": 68, "102": 69, "103": 70, "104": 70, "105": 70, "106": 71, "107": 71, "108": 73, "109": 77, "110": 81, "111": 81, "112": 81, "113": 81, "114": 81, "115": 81, "116": 86, "117": 86, "123": 117}}
__M_END_METADATA
"""
