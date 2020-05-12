# -*- coding: utf-8 -*-
from odoo import http

# class Cityview(http.Controller):
#     @http.route('/cityview/cityview/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cityview/cityview/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cityview.listing', {
#             'root': '/cityview/cityview',
#             'objects': http.request.env['cityview.cityview'].search([]),
#         })

#     @http.route('/cityview/cityview/objects/<model("cityview.cityview"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cityview.object', {
#             'object': obj
#         })