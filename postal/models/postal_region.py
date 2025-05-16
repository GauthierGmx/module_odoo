# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Region(models.Model):
    _name = 'postal.region'
    _description = 'Description of a region in France'

    name = fields.Char(string='Name', required=True)
    iso_3166_code = fields.Char(string='ISO 3166 Code', required=True)
    insee_code = fields.Char(string='INSEE Code', required=True)