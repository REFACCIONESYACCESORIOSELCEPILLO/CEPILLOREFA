# -*- coding: utf-8 -*-
import base64
import logging
import io

#from barcode import Code39
#from barcode.writer import ImageWriter
from odoo import api, models, fields, _, tools
from PIL import Image

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_open_label_layout(self):
        return self.env.ref('product_extesion_ref.action_custom_label_form').read()[0] 

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

    def get_custom_label(self):
        # get the report action back as we will need its data
        report = self.env['ir.actions.report']._get_report_from_name('product_extesion_ref.report_custom_label_product')
        # get the records selected for this rendering of the report
      #  obj = self.env[report.model].browse(docids)
        # return a custom rendering context
        return {
            'lines': docids.get_lines()
        }
#        return self.env.ref('product_extesion_ref.report_custom_label_product').report_Action(self)

    @api.depends('product_ref_ids')
    def compute_names_equivalence(self):
        self.names_equivalence = ''
        for equi in self.product_ref_ids:
            if equi.equivalence_id:
                self.names_equivalence += equi.equivalence_id.name + equi.equivalence_id.default_code + ' '
            elif equi.equivalence_extra:
                self.names_equivalence += equi.equivalence_extra + ' '

        print("############### NAMES EQUIVALENCE >>>>>>>>>>>>>>>>>> ", self.names_equivalence)

    names_equivalence = fields.Char(string="Names", compute="compute_names_equivalence")

    product_ref_ids = fields.One2many('product.template.equivalence', 'product_id', string="Equivalencia")
    car_ids = fields.Many2many('product.categ.car', string="Vehiculos")

    @api.model
    def _search_get_detail(self, website, order, options):
        car_domain = []
        product_tmpl_domain = []
        if search_brand := options.get('search_brand'):
            car_domain.append(('name', 'ilike', search_brand))
        if search_model := options.get('search_model'):
            car_domain.append(('modelo', 'ilike', search_model))

        if search_piece := options.get('search_piece'):
            car_domain.append(('name', 'ilike', search_piece))

        try:
            if search_year := options.get('search_year'):
                search_year = int(search_year)
                car_domain.append('&')
                car_domain.append(('start_year', '<=', search_year))
                car_domain.append(('end_year', '>=', search_year))
        except ValueError as _:
            pass

        skip = -3 if '&' in car_domain else -1
        for _ in range(len(car_domain) + skip):
            car_domain.insert(0, '|')

        if car_domain:
            car_ids = self.env['product.categ.car'].sudo().search(car_domain)
            product_tmpl_domain.append(('car_ids', 'in', car_ids.ids))

        res = super()._search_get_detail(website, order, options)
        res['base_domain'].append(product_tmpl_domain)
        res.update({'requires_sudo': True})
        return res


class ProductTemplateEquivalence(models.Model):
    _name = 'product.template.equivalence'

    product_id = fields.Many2one('product.template', string="Producto")
    equivalence_id = fields.Many2one('product.template', string="Equivalencia")
    equivalence_extra = fields.Char(string="Equivalencia extra")
    standard_price = fields.Float(string="Coste")
    list_price = fields.Float(string="Precio de venta")
    currency_id = fields.Many2one('res.currency', string="Moneda", related="equivalence_id.currency_id")

    @api.onchange('equivalence_id')
    def onchange_equivalence_id(self):
        if self.equivalence_id:
            self.standard_price = self.equivalence_id.standard_price
            self.list_price = self.equivalence_id.list_price


class ProductCategCar(models.Model):
    _name = 'product.categ.car'

    name = fields.Char(string="Nombre")
    modelo = fields.Char(string="Modelo")
    start_year = fields.Integer(string="Año inicio")
    end_year = fields.Integer(string="Año fin")
    version = fields.Char(string="Version")
