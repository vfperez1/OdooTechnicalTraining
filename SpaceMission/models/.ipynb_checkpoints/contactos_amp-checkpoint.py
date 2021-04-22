# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ContactosAmp(models.Model):
    _inherit = "res.partner"
    
    x_conceptos = fields.Char(string="Conceptos")
    x_concepto_1 = fields.Text()
    x_concepto_2 = fields.Char(string="Concepto 2")
    x_concepto_2 = fields.Char(string="Concepto 3")
    x_mantenimiento_d3 = fields.Boolean(string="Mantenimiento D3")
    x_actividad = fields.Integer(string="Activdad")
    x_telefono_2 = fields.Char()
    