# -*- coding: utf-8 -*-
import base64
import logging
import io

#from barcode import Code39
#from barcode.writer import ImageWriter
from odoo import api, models, fields, _, tools
from PIL import Image

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_blocked_quo = fields.Boolean(string="Bloqueado", default=False)

    def allow_edit_quo(self):
        for rec in self:
            flag = 1
            if rec.is_blocked_quo == True:
                rec.sudo().is_blocked_quo = False

    @api.model
    def create(self, vals):
        res = super(SaleOrder,self).create(vals)
        res.write({'is_blocked_quo': True})
        return res
    """
    def write(self, vals):
        res = super(SaleOrder,self).write(vals)
        for rec in self:
            if self.is_blocked_quo == False:
                rec.write({'is_blocked_quo': True})
        return res
    """
