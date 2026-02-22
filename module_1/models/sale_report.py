from odoo import models, fields


class SaleReport(models.Model):
    _inherit = "sale.report"

    suc_manantial = fields.Float(readonly=True)
    suc_magon = fields.Float(readonly=True)
    suc_poza_rica = fields.Float(readonly=True)
    suc_papantla = fields.Float(readonly=True)
    suc_tuxpan = fields.Float(readonly=True)

    def _select_additional_fields(self):
        res = super()._select_additional_fields()

        res.update({
            'suc_manantial': "CASE WHEN sl.branch = 'MAN' THEN 1 ELSE 0 END",
            'suc_magon': "CASE WHEN sl.branch = 'MAG' THEN 1 ELSE 0 END",
            'suc_poza_rica': "CASE WHEN sl.branch = 'POZ' THEN 1 ELSE 0 END",
            'suc_papantla': "CASE WHEN sl.branch = 'PAP' THEN 1 ELSE 0 END",
            'suc_tuxpan': "CASE WHEN sl.branch = 'TUX' THEN 1 ELSE 0 END",
        })

        return res

    def _from_sale(self):
        res = super()._from_sale()
        res += """
            LEFT JOIN stock_warehouse sh ON sh.id = s.warehouse_id
            LEFT JOIN stock_location sl ON sl.id = sh.lot_stock_id
        """
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += ", sl.branch"
        return res