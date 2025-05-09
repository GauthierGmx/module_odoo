# -*- coding: utf-8 -*-
# from odoo import http


# class Postal(http.Controller):
#     @http.route('/postal/postal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/postal/postal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('postal.listing', {
#             'root': '/postal/postal',
#             'objects': http.request.env['postal.postal'].search([]),
#         })

#     @http.route('/postal/postal/objects/<model("postal.postal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('postal.object', {
#             'object': obj
#         })

