# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554996944.615336
_enable_loop = True
_template_filename = '/Users/ericbeecher1/intex/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'main_content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        csrf_input = context.get('csrf_input', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def main_content():
            return render_main_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n\n<html lang="en">\n    <head>\n\n        <meta charset="utf-8">\n        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n\n    \t\t<title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('</title>\n\n        <link rel="shortcut icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/Intex2LogoWhite.png">\n\n        <!-- REQ: Bootstrap 4.x -->\n        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">\n\n\n        <!-- Font Awesome -->\n        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">\n\n        <!-- REQ: Jquery 3.3.x -->\n        <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>\n\n        <!-- REQ: Bootstrap 4.x -->\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>\n\n        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap4.min.css">\n\n        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>\n        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap4.min.js"></script>\n\n\n\n        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n\n\n\n\n\n\t</head>\n\n\t<body class="h-dark h-solid h-sticky h-nav-content-bottom h-show-icon-group">\n        ')

        if request.user.is_authenticated :
          if request.user.has_perm('perscriptions.can_crud') :
            home_url = '/perscriptions/drugs'
          else :
            home_url = '/perscriptions/'
        else:
          home_url = '/account/'
        
                
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['home_url'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n        <header>\n            <!-- header -->\n            <div class="container header-container">\n\n                <div class="header-search row">\n                    <form action="/perscriptions/search" method="post">\n                      ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( csrf_input ))
        __M_writer('\n                        <div class="row justify-content-center">\n\n                            <div class="col-5">\n                                <input type="text" name="search_term" class="form-control" value="" placeholder="Type and press enter">\n                            </div>\n                            <div class="col-2">\n                                <a href="#" class="submit-header-search"><span class="fas fa-chevron-circle-right"></span></a>\n                                <a href="#" class="toggle-header-search text-danger"><span class="fas fa-window-close"></span></a>\n                            </div>\n\n                        </div>\n                    </form>\n                </div>\n\n                <div class="logo"><a href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(home_url))
        __M_writer('"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/Intex2LogoWhite.png"  /></a></div>\n                <div class="mobile-logo"><a href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(home_url))
        __M_writer('"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/Intex2LogoWhite.png" /></a></div>\n\n                <div class="mobile-icon-group">\n                    <a href=""><span class="fas fa-search"></span></a>\n                    <a class="on-open-only" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(home_url))
        __M_writer('"><span class="fas fa-home"></span></a>\n                </div>\n                <div class="mobile-nav-trigger"><span class="close-icon fas fa-window-close"></span><span class="open-icon fas fa-bars"></span></div>\n\n                <div class="icon-group">\n')
        if request.user.is_authenticated :
            __M_writer('                  <a class="toggle-header-search" href="" data-toggle="tooltip" title="Search"><span class="fas fa-search"></span></a>\n                  <a class="text-secondary" target="_blank" href="/account/logout" data-toggle="tooltip" title="Logout"><span class="fas fa-sign-out-alt"></span></a>\n')
        else :
            __M_writer('                  <a class="text-secondary" target="_blank" href="/account/" data-toggle="tooltip" title="Login"><span class="fas fa-sign-in-alt"></span></a>\n')
        __M_writer('                </div>\n\n                <nav role="navigation">\n')
        if request.user.is_authenticated :
            __M_writer('                    <ul class="level-1 " style="">\n                      <li><a href="/perscriptions/drugs">Drugs</a></li>\n                      <li class="flyout">\n                        <a href="/perscriptions/prescribers" class="parent">Prescribers\n')
            if request.user.has_perm('perscriptions.can_crud') :
                __M_writer('                          <i class="carrot fas fa-angle-down"></i>\n')
            __M_writer('                        </a>\n')
            if request.user.has_perm('perscriptions.can_crud') :
                __M_writer('                        <ul class="level-2 row no-gutters list-unstyled" style="z-index: 100; display: none;">\n                          <li class=""><a href="/perscriptions/prescribers.add" class="">Add New Prescriber</a></li>\n                        </ul>\n')
            __M_writer('                      </li>\n                    </ul>\n')
        __M_writer('\n                </nav>\n\n            </div>\n\n            <div class="clearfix"></div>\n        </header>\n\n        <main>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_content'):
            context['self'].main_content(**pageargs)
        

        __M_writer('\n            <!-- END: CONTENT -->\n        </main>\n\n        <footer>\n            <section class="bg-dark-2">\n                <div class="container">\n                    <div class="row">\n                        <div class="col-12 text-center" style="color: #fff; opacity: .5; font-size: 80%;">&copy; Copyright 2019 Wells Institute. ALL RIGHTS RESERVED.</div>\n                    </div>\n                </div>\n            </section>\n        </footer>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_content():
            return render_main_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/ericbeecher1/intex/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "31": 1, "36": 9, "37": 11, "38": 11, "39": 35, "40": 35, "41": 44, "54": 53, "55": 60, "56": 60, "57": 75, "58": 75, "59": 75, "60": 75, "61": 76, "62": 76, "63": 76, "64": 76, "65": 80, "66": 80, "67": 85, "68": 86, "69": 88, "70": 89, "71": 91, "72": 94, "73": 95, "74": 99, "75": 100, "76": 102, "77": 103, "78": 104, "79": 108, "80": 111, "85": 122, "91": 9, "102": 120, "108": 120, "114": 108}}
__M_END_METADATA
"""
