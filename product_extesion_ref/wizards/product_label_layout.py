# -*- coding: utf-8 -*-
import logging
from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError
import io
from PIL import Image

_logger = logging.getLogger(__name__)


class CustomLabel(models.TransientModel):
    _name = 'product_extesion_ref.custom_label'

    @api.model
    def default_get(self, fields):
        vals = super(CustomLabel, self).default_get(fields)
        if self.env.context.get('active_model') == 'stock.picking':
            stock_picking = self.env['stock.picking'].browse(self.env.context.get('active_id'))
            if stock_picking:
                vals['picking_id'] = stock_picking.id
        elif self.env.context.get('active_model') == 'product.template':
            product_template = self.env['product.template'].browse(self.env.context.get('active_id'))
            if product_template:
                vals['product_id'] = product_template.id
        return vals


    print_format = fields.Selection([
        ('custom_label','Etiqueta Personalizada'),
        ('5x10', 'Etiqueta 5X10cm'),
        ('8x3','Etiqueta 8X3cm')
    ],string="Formato de etiqueta"
    )
    picking_id = fields.Many2one('stock.picking', string="Transferencia")
    product_id = fields.Many2one('product.template', string="Producto")

    width = fields.Integer(string="Ancho")
    height = fields.Integer(string="Alto")

    def get_width_px(self,width):
        if self.print_format == 'custom_label':
            width_px = (width * 118.1)/3
        elif self.print_format == '5x10':
            width_px = 197
        elif self.print_format == '8x3':
            width_px = 315
        return int(width_px)

    def get_height_px(self,height):
        if self.print_format == 'custom_label':
            height_px = ((height * 118.1)/3)/3
        elif self.print_format == '5x10':
            height_px = 33
        elif self.print_format == '8x3':
            height_px = 53
        
        _logger.error("***********height******"+str(height_px))
        return int(height_px)

    def action_confirm(self):
        for rec in self:
            if rec.picking_id:
                if rec.print_format == 'custom_label':
                    if rec.width <= 0 or rec.height <= 0:
                        raise ValidationError("El Largo o Ancho debe ser mayor a 0, verifique sus valores")
                    else:
                        return self.env.ref('product_extesion_ref.report_custom_label_picking_customizable').read()[0]
                elif rec.print_format == '5x10':
                    return self.env.ref('product_extesion_ref.report_custom_label_picking_5x10cm').read()[0]
                elif rec.print_format == '8x3':
                    return self.env.ref('product_extesion_ref.report_custom_label_picking_8x3cm').read()[0]
            elif rec.product_id:
                if rec.print_format == 'custom_label':
                    if rec.width <= 0 or rec.height <= 0:
                        raise ValidationError("El Largo o Ancho debe ser mayor a 0, verifique sus valores")
                    else:
                        return self.env.ref('product_extesion_ref.report_custom_label_product_customizable').read()[0]
                elif rec.print_format == '5x10':
                    return self.env.ref('product_extesion_ref.report_custom_label_product_5x10cm').read()[0]
                elif rec.print_format == '8x3':
                    return self.env.ref('product_extesion_ref.report_custom_label_product_8x3cm').read()[0]
            
                

    #METER VALIDACION DE TAMAÑO DE ANCHO Y LARGO CARTA?

    