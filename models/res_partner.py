# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    id_national = fields.Char('National id',size = 14)
    is_doctor = fields.Boolean(string="is a doctor ", default=False, help="If set, the .")