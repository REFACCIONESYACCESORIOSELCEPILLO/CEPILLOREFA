# -*- coding: utf-8 -*-
import logging
from odoo import api, models, fields, _

_logger = logging.getLogger(__name__)


class SaleReport(models.Model):
    _inherit = 'sale.report'

    # @api.depends('warehouse_id')
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

    
    suc_manantial = fields.Float(string="Suc. Manantial", readonly=True)
    suc_magon = fields.Float(string="Suc. Magon", readonly=True)
    suc_poza_rica = fields.Float(string="Suc. Poza Rica", readonly=True)
    suc_papantla = fields.Float(string="Suc. Papantla", readonly=True)
    suc_tuxpan = fields.Float(string="Suc. Tuxpan", readonly=True)


    def _select_sale(self):
        res = super()._select_sale()
        _logger.info('\n\n %r \n\n', res)
        res += """
            ,CASE WHEN sl.branch = 'MAN' THEN 1 ELSE 0
            END AS suc_manantial,
            CASE WHEN sl.branch = 'MAG' THEN 1 ELSE 0
            END AS suc_magon,
            CASE WHEN sl.branch = 'POZ' THEN 1 ELSE 0
            END AS suc_poza_rica,
            CASE WHEN sl.branch = 'PAP' THEN 1 ELSE 0
            END AS suc_papantla,
            CASE WHEN sl.branch = 'TUX' THEN 1 ELSE 0
            END AS suc_tuxpan
            """
        return res

    def _from_sale(self):
        res = super()._from_sale()
        res += """LEFT JOIN stock_warehouse sh ON sh.id = s.warehouse_id
                LEFT JOIN stock_location sl ON sl.id = sh.lot_stock_id
                """
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            sl.branch"""
        return res