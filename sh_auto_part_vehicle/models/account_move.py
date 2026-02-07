from odoo import fields,models



class Invoice(models.Model):


    _inherit="account.move"




    def viewSaleOrder(self, domain=None):
            # domain = domain or [['state', '=', 'sale']]  
            domain = domain or [["payment_state", "in", ["paid", "partial", "in_payment"]]]
            return {
                'name': 'Invoice',
                'type': 'ir.actions.act_window',
                'view_mode': 'list',
                'views': [(self.env.ref('account.view_out_invoice_tree').id, 'list')],  
                'res_model': 'account.move',
                'domain': domain or [],  
                'context': {'create': False},
                'target': 'current',
            }