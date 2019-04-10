# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554847320.4381042
_enable_loop = True
_template_filename = '/Users/ericbeecher1/intex/account/templates/index.html'
_template_uri = 'index.html'
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
        csrf_input = context.get('csrf_input', UNDEFINED)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def main_content():
            return render_main_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_content'):
            context['self'].main_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        csrf_input = context.get('csrf_input', UNDEFINED)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def main_content():
            return render_main_content(context)
        __M_writer = context.writer()
        __M_writer('\n<!-- BEGIN: CONTENT -->\n<section class="page-title bg-image bg-overlay d-lg-block d-md-block d-sm-none d-none" style="height: 300px; background-image: url(')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('account/media/doctor-arms.jpg); background-repeat: no-repeat;  background-size: cover; background-position: center -160px;">\n  <div class="overlay">\n    <div class="container">\n      <h1 class="text-right">Login</h1>\n    </div>\n  </div>\n</section>\n<section class="d-lg-none d-md-none d-sm-block d-xs-block" style="height: 180px; background-image: url(')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('account/media/doctor-arms.jpg); background-repeat: no-repeat; background-position: top;  background-size: cover;">\n  <div class="overlay">\n    <div class="container">\n      <h1 class="text-right" style="color: #fff">Login</h1>\n    </div>\n  </div>\n</section>\n<section>\n  <div class="row">\n    <div class="col-12 col-lg-4 offset-lg-4">\n      <div class="well">\n        <div class="inlay-form-labels">\n          <h4 class="text-secondary">\n          Login\n          </h4>\n          <div class="oak_contact_form_wrapper">\n            <div class="oak_contact_above_form">\n            </div>\n            <form method="post" class="oak_contact_form">\n                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( csrf_input ))
        __M_writer('\n                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_p()))
        __M_writer('\n                <button class="btn btn-primary btn-block" type="submit">Submit</button>\n            </form>\n          </div>\n\n        </div>\n\n      </div>\n    </div>\n  </div>\n</section>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/account/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 48, "51": 6, "61": 6, "62": 8, "63": 8, "64": 15, "65": 15, "66": 34, "67": 34, "68": 35, "69": 35, "75": 69}}
__M_END_METADATA
"""
