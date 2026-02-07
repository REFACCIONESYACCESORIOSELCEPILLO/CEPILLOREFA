# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields


class MotorcycleYear(models.Model):
    _name = "motorcycle.year"
    _description = "year"
    _order = "id desc"

    name = fields.Integer(string="Name", required=True)
    company_id = fields.Many2one(
        'res.company',
        string='Company'
    )
    website_id = fields.Many2one(
        'website',
        string='Website'
    )
