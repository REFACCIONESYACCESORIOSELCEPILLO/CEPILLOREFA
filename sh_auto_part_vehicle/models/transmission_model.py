# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models


class MotorcycleTransmission(models.Model):
    _name = "motorcycle.transmission"
    _description = "Motorcycle Transmission"
    _order = "sequence"

    name = fields.Char(required=True)
    sequence = fields.Integer(
        string=" "
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company'
    )
    website_id = fields.Many2one(
        'website',
        string='Website'
    )
