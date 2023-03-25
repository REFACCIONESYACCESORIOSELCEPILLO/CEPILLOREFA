# -*- coding: utf-8 -*-
import logging
from odoo import api, models, fields, _

_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # @api.depends('state')
    # def _get_location_products(self):
    #     for rec in self:
    #         if rec.warehouse_id.lot_stock_id.branch == 'MAN':
    #             rec.suc_manantial = 1
    #         else:
    #             rec.suc_manantial = 0
    #         if rec.warehouse_id.lot_stock_id.branch == 'MAG':
    #             rec.suc_magon = 1
    #         else:
    #             rec.suc_magon = 0
    #         if rec.warehouse_id.lot_stock_id.branch == 'POZ':
    #             rec.suc_poza_rica = 1
    #         else:
    #             rec.suc_poza_rica = 0
    #         if rec.warehouse_id.lot_stock_id.branch == 'PAP':
    #             rec.suc_papantla = 1
    #         else:
    #             rec.suc_papantla = 0
    #         if rec.warehouse_id.lot_stock_id.branch == 'TUX':
    #             rec.suc_tuxpan = 1
    #         else:
    #             rec.suc_tuxpan = 0

    
    suc_manantial = fields.Float(string="Suc. Manantial", related='product_id.suc_manantial', store=True)
    suc_magon = fields.Float(string="Suc. Magon", related='product_id.suc_magon', store=True)
    suc_poza_rica = fields.Float(string="Suc. Poza Rica", related='product_id.suc_poza_rica', store=True)
    suc_papantla = fields.Float(string="Suc. Papantla", related='product_id.suc_papantla', store=True)
    suc_tuxpan = fields.Float(string="Suc. Tuxpan", related='product_id.suc_tuxpan', store=True)


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
        fields['suc_manantial'] = ", l.suc_manantial as suc_manantial"
        groupby += ', l.suc_manantial'
        fields['suc_magon'] = ", l.suc_magon as suc_magon"
        groupby += ', l.suc_magon'
        fields['suc_poza_rica'] = ", l.suc_poza_rica as suc_poza_rica"
        groupby += ', l.suc_poza_rica'
        fields['suc_papantla'] = ", l.suc_papantla as suc_papantla"
        groupby += ', l.suc_papantla'
        fields['suc_tuxpan'] = ", l.suc_tuxpan as suc_tuxpan"
        groupby += ', l.suc_tuxpan'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)

    # def init(self):
    #     res = super(SaleReport, self).init()
    #     print("################## TABLE >>>>>>>>>>>>>>>>>>>>>>> ", self._table)
    #     print("CREATE or REPLACE VIEW %s as (%s)" % (self._table, self._query()))
    #     for product in self.env['product.product'].search([]):
    #         # val_product = False
    #         product_id = self.env['sale.report'].search([('product_id','=',product.id)])[0]
    #         self.env.cr.execute("""update sale_report set suc_manantial=0,
    #                                                       suc_magon=0,
    #                                                       suc_poza_rica=0,
    #                                                       suc_papantla=0,
    #                                                       suc_tuxpan=0 where product_id!= %s""" % (product.id))
                # if not val_product:
                #     report.suc_manantial = product.suc_manantial
                #     report.suc_magon = product.suc_magon
                #     report.suc_poza_rica = product.suc_poza_rica
                #     report.suc_papantla = product.suc_papantla
                #     report.suc_tuxpan = product.suc_tuxpan
            #         val_product = True
            #     else:
            #         report.suc_manantial = 0
            #         report.suc_magon = 0
            #         report.suc_poza_rica = 0
            #         report.suc_papantla = 0
            #         report.suc_tuxpan = 0
            # val_product = False
