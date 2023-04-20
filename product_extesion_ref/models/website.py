# -*- coding: utf-8 -*-
import logging
from odoo import api, models, fields, _

_logger = logging.getLogger(__name__)


class Website(models.Model):
    _inherit = 'website'

    qr_link = fields.Binary(string="QR dominio")
    secret = fields.Binary(string="base")