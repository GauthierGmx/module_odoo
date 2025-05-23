# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Departement(models.Model):
    _name = 'postal.departement'
    _description = 'Description of a department in France'

    name = fields.Char(string='Name', required=True)
    iso_3166_code = fields.Char(string='ISO 3166 Code', required=True)
    insee_code = fields.Char(string='INSEE Code', required=True)
    region_id = fields.Many2one('postal.region', string='Region', required=True)
    commune_ids = fields.One2many('postal.commune', 'departement_id', string='Cities')
    commune_count = fields.Integer(string='Number of Cities', compute='_compute_commune_count', store=True)

    @api.depends('commune_ids')
    def _compute_commune_count(self):
        for record in self:
            record.commune_count = len(record.commune_ids)