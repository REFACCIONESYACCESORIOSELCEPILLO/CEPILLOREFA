# -*- coding: utf-8 -*-
import base64
import logging
import io

#from barcode import Code39
#from barcode.writer import ImageWriter
from odoo import api, models, fields, _, tools
from PIL import Image

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def get_qr_link(self):
        for rec in self:
            qr = self.env['website'].search([('id','=',1)]).qr_link
            return qr

    def get_company_logo(self):
        for rec in self:
            logo = self.env['res.company'].search([('id','=',1)]).logo
            return logo

    def convert_cm_to_px(self, width, height):
        width_px = width * 118.1/3
        height_px = width_px/2
        base64_str = self.get_company_logo()
        buffer = io.BytesIO()
        imgdata = base64.b64decode(base64_str)
        img = Image.open(io.BytesIO(imgdata))
        new_img = img.resize((int(width_px), int(height_px)))  # x, y
        new_img.save(buffer, format="PNG")
        img_b64 = base64.b64encode(buffer.getvalue())
        return img_b64

    def convert_cm_to_px_qr(self, width, height):
        width_px = width * 118.1/3
        height_px = height * 118.1/3
        base64_str = self.get_qr_link()
        buffer = io.BytesIO()
        imgdata = base64.b64decode(base64_str)
        img = Image.open(io.BytesIO(imgdata))
        new_img = img.resize((int(width_px), int(height_px)))  # x, y
        new_img.save(buffer, format="PNG")
        img_b64 = base64.b64encode(buffer.getvalue())
        return img_b64


    def convert_main_img(self, width, height):
        qr = self.env['website'].search([('id','=',1)]).secret
        width_px = width * 118.1
        height_px = width_px * 118.1
        _logger.error("#########WIDTH######"+str(width_px))
        _logger.error("#########Height######"+str(height_px))
        base64_str = qr
        buffer = io.BytesIO()
        imgdata = base64.b64decode(base64_str)
        img = Image.open(io.BytesIO(imgdata))
        new_img = img.resize((int(width_px), int(height_px)))  # x, y
        new_img.save(buffer, format="PNG")
        img_b64 = base64.b64encode(buffer.getvalue())
        return img_b64
        

    def action_open_label_layout(self):
        return self.env.ref('product_extesion_ref.action_custom_label_form').read()[0]
