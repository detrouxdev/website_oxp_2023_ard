# -*- coding: utf-8 -*-
# from odoo import http


# class Oxp2023(http.Controller):
#     @http.route('/oxp_2023/oxp_2023', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oxp_2023/oxp_2023/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('oxp_2023.listing', {
#             'root': '/oxp_2023/oxp_2023',
#             'objects': http.request.env['oxp_2023.oxp_2023'].search([]),
#         })

#     @http.route('/oxp_2023/oxp_2023/objects/<model("oxp_2023.oxp_2023"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oxp_2023.object', {
#             'object': obj
#         })

