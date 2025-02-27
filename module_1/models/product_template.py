# -*- coding: utf-8 -*-
import logging
from odoo import api, models, fields, _

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.depends('qty_available')
    def _get_location_products(self):
        for rec in self:
            # rec.ensure_one()
            quant_ids = self.env['stock.quant'].search([('product_id.name','=',rec.name)])
            if not quant_ids:
                rec.suc_manantial = 0
                rec.suc_magon = 0
                rec.suc_poza_rica = 0
                rec.suc_papantla = 0
                rec.suc_tuxpan = 0
            for quant in quant_ids:
                if quant.location_id.branch == 'MAN' and quant.product_id.default_code == rec.default_code:
                    rec.suc_manantial = quant.quantity
                else:
                    rec.suc_manantial = rec.suc_manantial
                if quant.location_id.branch == 'MAG' and quant.product_id.default_code == rec.default_code:
                    rec.suc_magon = quant.quantity
                else:
                    rec.suc_magon = rec.suc_magon
                if quant.location_id.branch == 'POZ' and quant.product_id.default_code == rec.default_code:
                    rec.suc_poza_rica = quant.quantity
                else:
                    rec.suc_poza_rica = rec.suc_poza_rica
                if quant.location_id.branch == 'PAP' and quant.product_id.default_code == rec.default_code:
                    rec.suc_papantla = quant.quantity
                else:
                    rec.suc_papantla = rec.suc_papantla
                if quant.location_id.branch == 'TUX' and quant.product_id.default_code == rec.default_code:
                    rec.suc_tuxpan = quant.quantity
                else:
                    rec.suc_tuxpan = rec.suc_tuxpan

    suc_manantial = fields.Float(string="Suc. Manantial", compute=_get_location_products, default=0, store=True)
    suc_magon = fields.Float(string="Suc. Magon", compute=_get_location_products, default=0, store=True)
    suc_poza_rica = fields.Float(string="Suc. Poza Rica", compute=_get_location_products, default=0, store=True)
    suc_papantla = fields.Float(string="Suc. Papantla", compute=_get_location_products, default=0, store=True)
    suc_tuxpan = fields.Float(string="Suc. Tuxpan", compute=_get_location_products, default=0, store=True)

    sales_count = fields.Float(store=True)
    qty_available = fields.Float(store=True)
    virtual_available = fields.Float(store=True)
    incoming_qty = fields.Float(store=True)
    outgoing_qty = fields.Float(store=True)