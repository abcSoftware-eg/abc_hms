# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    abc_field = fields.Char(string="abc text")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        abc_field = self.env['ir.config_parameter'].sudo().get_param('abc_config.abc_field')
        res.update(
            abc_field=abc_field
        )
        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param('abc_config.abc_field', self.abc_field)
        super(ResConfigSettings, self).set_values()


