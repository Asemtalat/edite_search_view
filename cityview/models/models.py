# -*- coding: utf-8 -*-
from odoo import models, fields, api

class cityview(models.Model):
    _inherit = 'product.template'

    x_studio_city = fields.Char(string="City", required=False, )
    x_studio_valve = fields.Char(string="Valve", required=False, )
    x_studio_manifacture_date = fields.Char(string="Manifacture Date", required=False, )
    x_studio_capacityl = fields.Char(string="Capacity(L)", required=False, )
    x_studio_ = fields.Char(string="السابقة", required=False, )
