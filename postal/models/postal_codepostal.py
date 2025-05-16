# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Codepostal(models.Model):
    _name = 'postal.codepostal'
    _description = 'Description of a zip code in France'

    name = fields.Char(string='Zip code', required=True, size=5)
    commune_ids = fields.Many2many('postal.commune', string='Cities', required=True)
    commune_count = fields.Integer(string='Number of Cities', compute='_compute_commune_count', store=True)

    @api.depends('commune_ids')
    def _compute_commune_count(self):
        for record in self:
            record.commune_count = len(record.commune_ids)