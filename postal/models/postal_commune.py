# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Commune(models.Model):
    _name = 'postal.commune'
    _description = 'Description of a city in France'

    name = fields.Char(string='Name', required=True)
    type_commune = fields.Selection([
        ('ARM','Municipal district'),
        ('COM','Municipality'),
        ('COMA','Asociated municipality'),
        ('COMD','Delegated municipality'),    
    ],string="Type of city", required=True)
    insee_code = fields.Char(string='INSEE Code', required=True)
    departement_id = fields.Many2one('postal.departement',string='Department', required=True)
    codepostal_ids = fields.Many2many('postal.codepostal', string='Zip codes', required=True)

    # Hierarchical relationship between municipalities
    parent_id = fields.Many2one('postal.commune', string='Parent Municipality',ondelete='restrict')
    child_ids = fields.One2many('postal.commune', 'parent_id', string='Child Municipalities')