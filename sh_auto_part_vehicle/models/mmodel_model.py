# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import models, fields


class MotorcycleMmodel(models.Model):
    _name = "motorcycle.mmodel"
    _description = "mmodel"
    _order = "id desc"

    name = fields.Char(string="Name", required=True)
    make_id = fields.Many2one(
        comodel_name="motorcycle.make",
        string="Make", required=True,
        domain="[('website_id', '=', website_id), ('company_id', '=', company_id)]"
    )
    type_id = fields.Many2one(
        comodel_name="motorcycle.type",
        string="Type", required=True,
        domain="[('website_id', '=', website_id), ('company_id', '=', company_id)]"
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company'
    )
    website_id = fields.Many2one(
        'website',
        string='Website'
    )


    def viewVehicleModel(self,domain=None):
        return {
            'name': 'VehicleModel',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'views': [(self.env.ref('sh_auto_part_vehicle.sh_motorcycle_mmodel_tree').id,'list'),
                      (self.env.ref('sh_auto_part_vehicle.sh_motorcycle_mmodel_form').id,'form')],
            'domain': domain or [],
            'res_model': 'motorcycle.mmodel',
            'context': dict(create=False),
            'target': 'current',
        }
    


    



   

