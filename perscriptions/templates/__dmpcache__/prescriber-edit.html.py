# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554910757.299408
_enable_loop = True
_template_filename = '/Users/ericbeecher1/intex/perscriptions/templates/prescriber-edit.html'
_template_uri = 'prescriber-edit.html'
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
        message = context.get('message', UNDEFINED)
        def main_content():
            return render_main_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
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
        def page_title():
            return render_page_title(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('Edit: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Fname))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Lname))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        message = context.get('message', UNDEFINED)
        def main_content():
            return render_main_content(context)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <section>\n      <div class="container">\n        <div class="row">\n        <div class="col-12">\n          ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self, extra={'n_filter_on': True})(message ))
        __M_writer('\n          <h1 class="border-bottom mb-4 pb-1" style="border-bottom-style: dotted!important;">\n              ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Fname))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Lname))
        __M_writer('\n          </h1>\n        </div>\n\n          <div class="col-6">\n\n            <h3> Edit Details</h3>\n            <div class="well">\n              <form class="oak_contact_form" method="post">\n                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( csrf_input ))
        __M_writer('\n                <div class="row">\n\n')
        for field in form.visible_fields():
            __M_writer('                        <div class="col-lg-6 col-12 form-group">\n                        <label>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( field.label ))
            __M_writer('</label>\n                            ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( field ))
            __M_writer('\n                        </div>\n')
        __M_writer('                    <div class="col-12 text-center col-lg-6 offset-lg-3">\n                      <button class="btn btn-primary btn-block" type="submit">Update ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Fname))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Lname))
        __M_writer('</button>\n                    </div>\n\n\n                </div>\n              </form>\n            </div>\n\n\n          </div>\n          <div class="col-12 col-lg-6">\n            <h3> Edit Drugs Prescribed</h3>\n            <table class="datatable table table-striped table-bordered no-footer box-shadow">\n              <thead>\n                <tr>\n                <th class="nosort" style="width: 30px; text-align:center">\n\n                </th>\n                  <th>\n                    Name\n                  </th>\n                  <th class="text-center">\n                    # Prescribed\n                  </th>\n                  <th class="text-center">\n                    Actions\n                  </th>\n                </tr>\n\n              </thead>\n              <tbody>\n\n')
        for prescription in prescriber.get_drugs_perscribed():
            __M_writer('                  <tr>\n                    <td class="text-center">\n')
            if prescription.Drug.isOpioid:
                __M_writer('                        <i class="fas fa-capsules" data-toggle="tooltip" title="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Drug.DrugName.capitalize()))
                __M_writer(' is an Opioid"></i>\n')
            __M_writer('                    </td>\n                    <td>\n                      <a href="/perscriptions/prescriptions.edit/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.id))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.Drug.DrugName.capitalize()))
            __M_writer('</a>\n                    </td>\n                    <td class="text-center">\n                      ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.QuanityPerscribed))
            __M_writer('\n                    </td>\n                    <td class="text-center">\n                      <a href="/perscriptions/prescriptions.edit/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.id))
            __M_writer('" class="btn btn-success btn-sm"><i class="fas fa-edit"></i></a>\n                      <a href="/perscriptions/prescriptions.delete/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescription.id))
            __M_writer('" class="btn btn-danger btn-sm"><i class="fas fa-trash"></i></a>\n                    </td>\n                  </tr>\n')
        __M_writer('              </tbody>\n            </table>\n\n            <div class="row">\n              <div class="col-lg-6 col-12 offset-lg-3">\n                <a href="/perscriptions/prescriptions.add/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.id))
        __M_writer('" class="btn btn-primary btn-block">Add A Perscription for ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Fname))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Lname))
        __M_writer('</a>\n              </div>\n            </div>\n          </div>\n\n        </div>\n      </div>\n    </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/perscriptions/templates/prescriber-edit.html", "uri": "prescriber-edit.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 2, "53": 93, "59": 2, "67": 2, "68": 2, "69": 2, "70": 2, "76": 3, "87": 3, "88": 8, "89": 8, "90": 10, "91": 10, "92": 10, "93": 10, "94": 19, "95": 19, "96": 22, "97": 23, "98": 24, "99": 24, "100": 25, "101": 25, "102": 28, "103": 29, "104": 29, "105": 29, "106": 29, "107": 61, "108": 62, "109": 64, "110": 65, "111": 65, "112": 65, "113": 67, "114": 69, "115": 69, "116": 69, "117": 69, "118": 72, "119": 72, "120": 75, "121": 75, "122": 76, "123": 76, "124": 80, "125": 85, "126": 85, "127": 85, "128": 85, "129": 85, "130": 85, "136": 130}}
__M_END_METADATA
"""
