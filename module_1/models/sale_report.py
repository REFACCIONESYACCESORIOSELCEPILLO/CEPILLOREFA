from odoo import models, fields


class SaleReport(models.Model):
    _inherit = "sale.report"

    suc_manantial = fields.Float(readonly=True)
    suc_magon = fields.Float(readonly=True)
    suc_poza_rica = fields.Float(readonly=True)
    suc_papantla = fields.Float(readonly=True)
    suc_tuxpan = fields.Float(readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['suc_manantial'] = ", CASE WHEN sl.branch = 'MAN' THEN 1 ELSE 0 END"
        fields['suc_magon'] = ", CASE WHEN sl.branch = 'MAG' THEN 1 ELSE 0 END"
        fields['suc_poza_rica'] = ", CASE WHEN sl.branch = 'POZ' THEN 1 ELSE 0 END"
        fields['suc_papantla'] = ", CASE WHEN sl.branch = 'PAP' THEN 1 ELSE 0 END"
        fields['suc_tuxpan'] = ", CASE WHEN sl.branch = 'TUX' THEN 1 ELSE 0 END"

        from_clause += """
            LEFT JOIN stock_warehouse sh ON sh.id = s.warehouse_id
            LEFT JOIN stock_location sl ON sl.id = sh.lot_stock_id
        """

        groupby += ", sl.branch"

        return super()._query(with_clause, fields, groupby, from_clause)