from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
	_inherit = "sale.order"

	blocked_order = fields.Boolean(string="Order blocked")

	def action_unlock_order(self):
		self.with_context(unlock=True).blocked_order = False

	@api.model_create_multi
	def create(self, vals_list):
		for vals in vals_list:
			if not vals.get('website_id', False):
				vals['blocked_order'] = True
		return super().create(vals_list)

	def write(self, values):
		if ('website_id' in self._fields and not self.website_id) or 'website_id' not in self._fields:
			if ('state' in values and values.get('state') != 'draft') or self._context.get('unlock',False):
				values['blocked_order'] = False
			else:
				values['blocked_order'] = True
			# raise UserError("No puede modificar ningun registro, solicite desbloqueo al Responsable")
		return super().write(values)