# -*- coding: utf-8 -*-
# from odoo import http


# class AbcHms(http.Controller):
#     @http.route('/abc_hms/abc_hms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_hms/abc_hms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_hms.listing', {
#             'root': '/abc_hms/abc_hms',
#             'objects': http.request.env['abc_hms.abc_hms'].search([]),
#         })

#     @http.route('/abc_hms/abc_hms/objects/<model("abc_hms.abc_hms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_hms.object', {
#             'object': obj
#         })
