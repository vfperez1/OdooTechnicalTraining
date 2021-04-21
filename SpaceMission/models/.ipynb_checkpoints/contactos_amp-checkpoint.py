# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ContactosAmp(models.Model):
    _inherit = "res.partner"
    
    conceptos = fields.Char(string="Conceptos")
    concepto_1 = fields.Char(string="Concepto 1")
    concepto_2 = fields.Char(string="Concepto 2")
    concepto_2 = fields.Char(string="Concepto 3")
    mantenimiento_d3 = fields.Boolean(string="Mantenimiento D3")
    actividad = fields.Integer(string="Activdad")
    