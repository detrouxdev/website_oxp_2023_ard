# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class oxp_2023(models.Model):
#     _name = 'oxp_2023.oxp_2023'
#     _description = 'oxp_2023.oxp_2023'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

