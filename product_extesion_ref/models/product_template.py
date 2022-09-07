# -*- coding: utf-8 -*-
import logging
from odoo import api, models, fields, _

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_ref_ids = fields.One2many('product.template.equivalence', 'product_id', string="Equivalencia")
    car_ids = fields.Many2many('product.categ.car', string="Vehiculos")

class ProductTemplateEquivalence(models.Model):
    _name = 'product.template.equivalence'

    product_id = fields.Many2one('product.template', string="Producto")
    equivalence_id = fields.Many2one('product.template', string="Equivalencia")
    equivalence_extra = fields.Char(string="Equivalencia extra")
    standard_price = fields.Float(string="Coste")
    list_price = fields.Float(string="Precio de venta")
    currency_id = fields.Many2one('res.currency', string="Moneda", related="equivalence_id.currency_id")

    @api.onchange('equivalence_id')
    def onchange_equivalence_id(self):
        if self.equivalence_id:
            self.standard_price = self.equivalence_id.standard_price
            self.list_price = self.equivalence_id.list_price

class ProductCategCar(models.Model):
    _name = 'product.categ.car'

    name = fields.Char(string="Nombre")
    modelo = fields.Char(string="Modelo")
    año = fields.Char(string="Año inicio")
    age_end = fields.Char(string="Año fin")
    version = fields.Char(string="Version")