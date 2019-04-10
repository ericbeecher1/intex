# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554929638.05181
_enable_loop = True
_template_filename = '/Users/ericbeecher1/intex/perscriptions/templates/search.html'
_template_uri = 'search.html'
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
        search_term = context.get('search_term', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        prescriber_results = context.get('prescriber_results', UNDEFINED)
        drug_results = context.get('drug_results', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('Search Results')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_content():
            return render_main_content(context)
        search_term = context.get('search_term', UNDEFINED)
        prescriber_results = context.get('prescriber_results', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        drug_results = context.get('drug_results', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <section>\n      <div class="container">\n        <div class="row">\n          <div class="col-12 mb-4">\n            <form method="post">\n              ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( csrf_input ))
        __M_writer('\n              <div class="input-group">\n                <input type="text" class="form-control" name="search_term" placeholder="New Search" aria-label="New Search" aria-describedby="basic-addon2" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(search_term))
        __M_writer('">\n                <div class="input-group-append">\n                  <button class="btn btn-primary" type="submit" type="button"><i class="fas fa-search"></i></button>\n                </div>\n              </div>\n            </form>\n          </div>\n          <div class="col-12">\n            <ul class="nav nav-tabs mb-3">\n              <li class="nav-item">\n                <a class="nav-link active" data-toggle="tab" role="tab" href="#drug_results">Drugs</a>\n              </li>\n              <li class="nav-item">\n                <a class="nav-link" data-toggle="tab" role="tab" href="#prescriber_results">Perscribers</a>\n              </li>\n            </ul>\n          </div>\n          <div class="col-12">\n            <div class="tab-content w-100" id="myTabContent">\n              <div class="tab-pane fade active show" id="drug_results" role="tabpanel" aria-labelledby="profile-tab">\n              <table class="datatable table table-striped table-bordered no-footer">\n                <thead>\n                  <tr>\n                    <th class="nosort" style="width: 30px">\n\n                    </th>\n                    <th>\n                      Drug Name\n                    </th>\n                    <th class="nosort" style="text-align: center">\n                      Action\n                    </th>\n                  </tr>\n\n                </thead>\n                <tbody>\n')
        for drug in drug_results:
            __M_writer('                    <tr>\n                      <td class="text-center">\n')
            if drug.isOpioid:
                __M_writer('                          <i class="fas fa-capsules" data-toggle="tooltip" title="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.DrugName.capitalize()))
                __M_writer(' is an Opioid"></i>\n')
            __M_writer('                      </td>\n                      <td class="text-capitalize">\n                        <a href="/perscriptions/drugs.details/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.id))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.DrugName.lower()))
            __M_writer('</a>\n                      </td>\n                      <td class="actions_cell">\n                        <a href="/perscriptions/drugs.details/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug.id))
            __M_writer('" class="btn btn-light btn-sm"><i class="fas fa-eye"></i></a>\n                      </td>\n                    </tr>\n\n')
        __M_writer('                </tbody>\n              </table>\n\n              </div>\n              <div class="tab-pane fade" id="prescriber_results" role="tabpanel" aria-labelledby="contact-tab">\n                <table class="datatable table table-striped table-bordered no-footer">\n                  <thead>\n                    <tr>\n                      <th class="nosort" style="width: 30px">\n\n                      </th>\n')
        if request.user.has_perm('perscriptions.can_see_names') :
            __M_writer('                        <th>\n                          Name\n                        </th>\n')
        else:
            __M_writer('                        <th>\n                          Doctor ID\n                        </th>\n')
        __M_writer('                      <th>\n                        Location\n                      </th>\n                      <th>\n                        Credentials\n                      </th>\n                      <th>\n                        Specialty\n                      </th>\n\n                      <th class="nosort" style="text-align: center">\n                        Actions\n                      </th>\n                    </tr>\n\n                  </thead>\n                  <tbody>\n')
        for prescriber in prescriber_results:
            __M_writer('                      <tr>\n                        <td class="text-center">\n\n                        </td>\n')
            if request.user.has_perm('perscriptions.can_see_names') :
                __M_writer('                          <td>\n                            <a href="/perscriptions/prescribers.view/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.id))
                __M_writer('">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Fname))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Lname))
                __M_writer('</a>\n                          </td>\n')
            else:
                __M_writer('                          <td>\n                            <a href="/perscriptions/prescribers.view/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.id))
                __M_writer('">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.DoctorID))
                __M_writer('</a>\n                          </td>\n')
            __M_writer('                        <td>\n                          ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.State))
            __M_writer('</a>\n                        </td>\n                        <td>\n                          ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Credentials))
            __M_writer('</a>\n                        </td>\n                        <td>\n                          ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.Specialty))
            __M_writer('</a>\n                        </td>\n                        <td class="text-center">\n                          <a href="/perscriptions/prescribers.view/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.id))
            __M_writer('" class="btn btn-light btn-sm"><i class="fas fa-eye"></i></a>\n')
            if request.user.has_perm('perscriptions.can_crud') :
                __M_writer('                            <a href="/perscriptions/prescribers.edit/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.id))
                __M_writer('" class="btn btn-success btn-sm"><i class="fas fa-edit"></i></a>\n                            <a href="/perscriptions/prescribers.delete/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.id))
                __M_writer('" onclick="confirm(\'Are you sure? This cannot be undone\')" class="btn btn-danger btn-sm"><i class="fas fa-trash"></i></a>\n')
            __M_writer('                        </td>\n                      </tr>\n\n')
        __M_writer('                  </tbody>\n                </table>\n              </div>\n            </div>\n          </div>\n\n\n\n          </div>\n\n      </div>\n    </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/perscriptions/templates/search.html", "uri": "search.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 2, "54": 145, "60": 2, "66": 2, "72": 3, "84": 3, "85": 9, "86": 9, "87": 11, "88": 11, "89": 47, "90": 48, "91": 50, "92": 51, "93": 51, "94": 51, "95": 53, "96": 55, "97": 55, "98": 55, "99": 55, "100": 58, "101": 58, "102": 63, "103": 74, "104": 75, "105": 78, "106": 79, "107": 83, "108": 100, "109": 101, "110": 105, "111": 106, "112": 107, "113": 107, "114": 107, "115": 107, "116": 107, "117": 107, "118": 109, "119": 110, "120": 111, "121": 111, "122": 111, "123": 111, "124": 114, "125": 115, "126": 115, "127": 118, "128": 118, "129": 121, "130": 121, "131": 124, "132": 124, "133": 125, "134": 126, "135": 126, "136": 126, "137": 127, "138": 127, "139": 129, "140": 133, "146": 140}}
__M_END_METADATA
"""
