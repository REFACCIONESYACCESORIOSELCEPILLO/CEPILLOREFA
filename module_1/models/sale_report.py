from odoo import models, fields


class SaleReport(models.Model):
    _inherit = "sale.report"

    suc_manantial = fields.Float(string="Suc. Manantial", readonly=True)
    suc_magon = fields.Float(string="Suc. Magon", readonly=True)
    suc_poza_rica = fields.Float(string="Suc. Poza Rica", readonly=True)
    suc_papantla = fields.Float(string="Suc. Papantla", readonly=True)
    suc_tuxpan = fields.Float(string="Suc. Tuxpan", readonly=True)

    # ---------------- SALE ----------------

    def _select_sale(self):
        res = super()._select_sale()
        res += """
            ,CASE WHEN sl.branch = 'MAN' THEN 1 ELSE 0 END AS suc_manantial
            ,CASE WHEN sl.branch = 'MAG' THEN 1 ELSE 0 END AS suc_magon
            ,CASE WHEN sl.branch = 'POZ' THEN 1 ELSE 0 END AS suc_poza_rica
            ,CASE WHEN sl.branch = 'PAP' THEN 1 ELSE 0 END AS suc_papantla
            ,CASE WHEN sl.branch = 'TUX' THEN 1 ELSE 0 END AS suc_tuxpan
        """
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

    # ---------------- POS (IMPORTANTE PARA EL UNION) ----------------

    def _select_pos_sale(self):
        res = super()._select_pos_sale()
        res += """
            ,0 AS suc_manantial
            ,0 AS suc_magon
            ,0 AS suc_poza_rica
            ,0 AS suc_papantla
            ,0 AS suc_tuxpan
        """
        return res