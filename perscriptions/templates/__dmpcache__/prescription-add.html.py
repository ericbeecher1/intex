# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555026463.080916
_enable_loop = True
_template_filename = '/Users/ericbeecher1/intex/perscriptions/templates/prescription-add.html'
_template_uri = 'prescription-add.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'main_content']


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
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_content'):
            context['self'].main_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        prescriber = context.get('prescriber', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('Add Perscription for: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Fname))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Lname))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_content():
            return render_main_content(context)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <section>\n      <div class="container">\n        <div class="row">\n        <div class="col-12">\n          <h1 class="border-bottom mb-4 pb-1" style="border-bottom-style: dotted!important;">\n              Add Perscription for: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Fname))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Lname))
        __M_writer('\n          </h1>\n        </div>\n\n          <div class="col-12">\n            <div class="well">\n              <form class="oak_contact_form" method="post">\n                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( csrf_input ))
        __M_writer('\n                <div class="row">\n                  <div class="col-lg-6 col-12 form-group">\n                    <label>Perscriber</label>\n                    <h5>\n                      ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Fname))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Lname))
        __M_writer('\n                    </h5>\n                  </div>\n')
        for field in form.visible_fields():
            __M_writer('                        <div class="col-lg-6 col-12 form-group">\n                        <label>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( field.label ))
            __M_writer('</label>\n                            ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( field ))
            __M_writer('\n                        </div>\n')
        __M_writer('                    <div class="col-12 text-center col-lg-4 offset-lg-4">\n                      <button class="btn btn-primary btn-block" type="submit">Update</button>\n                    </div>\n\n\n                </div>\n              </form>\n            </div>\n          </div>\n\n\n        </div>\n      </div>\n    </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/perscriptions/templates/prescription-add.html", "uri": "prescription-add.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 2, "52": 44, "58": 2, "66": 2, "67": 2, "68": 2, "69": 2, "75": 3, "85": 3, "86": 9, "87": 9, "88": 9, "89": 9, "90": 16, "91": 16, "92": 21, "93": 21, "94": 21, "95": 21, "96": 24, "97": 25, "98": 26, "99": 26, "100": 27, "101": 27, "102": 30, "108": 102}}
__M_END_METADATA
"""
