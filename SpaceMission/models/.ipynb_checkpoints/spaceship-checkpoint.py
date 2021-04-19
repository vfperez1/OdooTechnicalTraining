# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    
    _name = "space.ship"
    _description = "Modelo para la MisionEspacial del Technical Training"
    
    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    
    fuel_leo = fields.Integer(string="fuel", required=True) # Combustible para poner en órbita
    fuel_return = fields.Integer(string="fuel_return", required=True) # combustible de retorno
    diameter = fields.Integer(string="diameter", required=True)
    length = fields.Integer(string="length", required=True) # Longitud
    mass = fields.Integer(string="mass", required=True) # Masa
    engines = fields.Integer(string="engines", required=True) # Motores
    push = fields.Integer(string="push", required=True) # Empuje
    propellant_capacity = fields.Integer(string="propellant_capacity", required=True) # Capacidad de propulsor
    weight = fields.Integer(string="weight", required=True)
    pasajeros = fields.Integer(string="weight", required=True)
    
    prototipos = fields.Selection(string="prototipos",
                                 selection=[("starship_mk1", "Starship Mk1" ),
                                           ("starship_sn1", "Starship SN1"),
                                           ("starship_sn2", "Starship SN2"),
                                           ("starship_sn3", "Starship SN3"),
                                           ("starship_sn4", "Starship SN4")],
                                        copy=False)
    
    active = fields.Boolean(string="Active", default=True)