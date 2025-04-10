from odoo import models, fields, api
from odoo.exceptions import ValidationError

class WizardSOrder(models.TransientModel):
    _name = "wizard.sorder.report"
    _description = "Wizard Orden de Venta Reporte"

    name = fields.Char("Nombre")
    date_from = fields.Date("Desde Fecha")
    date_to = fields.Date("Hasta Fecha")
    warehouse_ids = fields.Many2many("stock.warehouse",string="Almacén")
    sale_order_line_ids = fields.Many2many("sale.order.line",string="Lineas")
    def print_report(self):
        if not self.date_from:
            raise ValidationError("Desde Fecha Requerido")
        domain = [('display_type','=',False),('product_template_id','!=',False),('invoice_status','=','invoiced'),('order_id.date_order','>=',self.date_from)]
        if self.date_to:
            domain.append(('order_id.date_order','<=',self.date_to))
        if self.warehouse_ids:
            domain.append(('warehouse_id','in',self.warehouse_ids.ids))

        lines = self.env["sale.order.line"].search(domain)        
        self.sale_order_line_ids = lines
        return self.env.ref('sale_order_report_custom.action_report_wizard_sorder_report').report_action(self)