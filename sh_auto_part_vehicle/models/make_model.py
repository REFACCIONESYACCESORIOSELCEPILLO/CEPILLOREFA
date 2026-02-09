# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import models, fields


class MotorcycleMake(models.Model):
    _name = "motorcycle.make"
    _description = 'make model'
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    company_id = fields.Many2one(
        'res.company',
        string='Company'
    )
    website_id = fields.Many2one(
        'website',
        string='Website'
    )



    

    def viewVehicleMake(self,domain=None):
        return {
            'name': 'VehicleMake',
            'type': 'ir.actions.act_window',
            'view_mode': 'list',
            'views': [(self.env.ref('sh_auto_part_vehicle.sh_motorcycle_make_tree').id,'list')],
            'domain': domain or [],
            'res_model': 'motorcycle.make',
            'context': dict(create=False),
            'target': 'current',
        }
    
