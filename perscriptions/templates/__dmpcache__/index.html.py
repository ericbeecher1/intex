# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554996546.2375638
_enable_loop = True
_template_filename = '/Users/ericbeecher1/intex/perscriptions/templates/index.html'
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
        prescriber = context.get('prescriber', UNDEFINED)
        def main_content():
            return render_main_content(context._locals(__M_locals))
        health_offical = context.get('health_offical', UNDEFINED)
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
        health_offical = context.get('health_offical', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <section>\n    <div class="container-fluid">\n')
        if health_offical:
            __M_writer("    <div class='tableauPlaceholder' id='viz1554995404007' style='position: relative'>\n      <noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;TN&#47;TN4QY47BC&#47;1_rss.png' style='border: none' /></a></noscript>\n      <object class='tableauViz'  style='display:none;'>\n        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />\n        <param name='embed_code_version' value='3' />\n        <param name='path' value='shared&#47;TN4QY47BC' />\n        <param name='toolbar' value='yes' />\n        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;TN&#47;TN4QY47BC&#47;1.png' />\n        <param name='animate_transition' value='yes' />\n        <param name='display_static_image' value='yes' />\n        <param name='display_spinner' value='yes' />\n        <param name='display_overlay' value='yes' />\n        <param name='display_count' value='yes' />\n      </object>\n    </div>\n    <script type='text/javascript'>\n      var divElement = document.getElementById('viz1554995404007');\n      var vizElement = divElement.getElementsByTagName('object')[0];\n      if ( divElement.offsetWidth > 800 )\n      { vizElement.style.width='1400px';vizElement.style.height='1027px';}\n      else if ( divElement.offsetWidth > 500 )\n      { vizElement.style.width='1400px';vizElement.style.height='1027px';}\n      else { vizElement.style.width='100%';vizElement.style.height='1677px';}\n      var scriptElement = document.createElement('script');\n      scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';\n      vizElement.parentNode.insertBefore(scriptElement, vizElement);\n    </script>\n")
        elif prescriber:
            __M_writer("      <div class='tableauPlaceholder' id='viz1554995438666' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;PrescriberView&#47;PrescriberDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PrescriberView&#47;PrescriberDashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;PrescriberView&#47;PrescriberDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1554995438666');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1400px';vizElement.style.height='1027px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1400px';vizElement.style.height='1027px';} else { vizElement.style.width='100%';vizElement.style.height='1727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>\n\n\n\n")
        __M_writer('    </div>\n  </section>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/perscriptions/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 43, "49": 3, "57": 3, "58": 6, "59": 7, "60": 34, "61": 35, "62": 40, "68": 62}}
__M_END_METADATA
"""
