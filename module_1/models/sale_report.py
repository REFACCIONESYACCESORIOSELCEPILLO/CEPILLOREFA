# -*- coding: utf-8 -*-
import logging
from odoo import api, models, fields, _

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('warehouse_id')
    def _get_location_products(self):
        for rec in self:
            if rec.warehouse_id.lot_stock_id.branch == 'MAN':
                rec.suc_manantial = 1
            else:
                rec.suc_manantial = 0
            if rec.warehouse_id.lot_stock_id.branch == 'MAG':
                rec.suc_magon = 1
            else:
                rec.suc_magon = 0
            if rec.warehouse_id.lot_stock_id.branch == 'POZ':
                rec.suc_poza_rica = 1
            else:
                rec.suc_poza_rica = 0
            if rec.warehouse_id.lot_stock_id.branch == 'PAP':
                rec.suc_papantla = 1
            else:
                rec.suc_papantla = 0
            if rec.warehouse_id.lot_stock_id.branch == 'TUX':
                rec.suc_tuxpan = 1
            else:
                rec.suc_tuxpan = 0

    
    suc_manantial = fields.Float(string="Suc. Manantial", compute=_get_location_products, store=True)
    suc_magon = fields.Float(string="Suc. Magon", compute=_get_location_products, store=True)
    suc_poza_rica = fields.Float(string="Suc. Poza Rica", compute=_get_location_products, store=True)
    suc_papantla = fields.Float(string="Suc. Papantla", compute=_get_location_products, store=True)
    suc_tuxpan = fields.Float(string="Suc. Tuxpan", compute=_get_location_products, store=True)


class SaleReport(models.Model):
    _inherit = 'sale.report'

#     @api.depends('warehouse_id')
#     def _get_location_products(self):
#         for rec in self:
#             rec.ensure_one()
#             if self.warehouse_id.lot_stock_id.branch == 'MAN':
#                 self.suc_manantial = 1
#             else:
#                 self.suc_manantial = 0
#             if self.warehouse_id.lot_stock_id.branch == 'MAG':
#                 self.suc_magon = 1
#             else:
#                 self.suc_magon = 0
#             if self.warehouse_id.lot_stock_id.branch == 'POZ':
#                 self.suc_poza_rica = 1
#             else:
#                 self.suc_poza_rica = 0
#             if self.warehouse_id.lot_stock_id.branch == 'PAP':
#                 self.suc_papantla = 1
#             else:
#                 self.suc_papantla = 0
#             if self.warehouse_id.lot_stock_id.branch == 'TUX':
#                 self.suc_tuxpan = 1
#             else:
#                 self.suc_tuxpan = 0

    
    suc_manantial = fields.Float(string="Suc. Manantial", store=True)
    suc_magon = fields.Float(string="Suc. Magon", store=True)
    suc_poza_rica = fields.Float(string="Suc. Poza Rica", store=True)
    suc_papantla = fields.Float(string="Suc. Papantla", store=True)
    suc_tuxpan = fields.Float(string="Suc. Tuxpan", store=True)

    
    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['suc_manantial'] = ", s.suc_manantial as suc_manantial"
        groupby += ', s.suc_manantial'
        fields['suc_magon'] = ", s.suc_magon as suc_magon"
        groupby += ', s.suc_magon'
        fields['suc_poza_rica'] = ", s.suc_poza_rica as suc_poza_rica"
        groupby += ', s.suc_poza_rica'
        fields['suc_poza_rica'] = ", s.suc_poza_rica as suc_poza_rica"
        groupby += ', s.suc_poza_rica'
        fields['suc_papantla'] = ", s.suc_papantla as suc_papantla"
        groupby += ', s.suc_papantla'
        fields['suc_tuxpan'] = ", s.suc_tuxpan as suc_tuxpan"
        groupby += ', s.suc_tuxpan'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)