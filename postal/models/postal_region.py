# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Region(models.Model):
    _name = 'postal.region'
    _description = 'Description of a region in France'

    name = fields.Char(string='Name', required=True)
    iso_3166_code = fields.Char(string='ISO 3166 Code', required=True)
    insee_code = fields.Char(string='INSEE Code', required=True, size=2)

    @api.constrains('insee_code')
    def _check_insee_code(self):
        for record in self:
            if not record.insee_code.isdigit() or len(record.insee_code) != 2:
                raise ValidationError("The INSEE code must be a 2-digit number.")