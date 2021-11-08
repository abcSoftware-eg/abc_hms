# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" + " " + str(rd.months) + "m" + " " + str(rd.days) + "d"
            else:
                rec.age = "No Date Of Birth!!"

    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Char(compute=onchange_age, string="Patient Age", store=True)
    id_national = fields.Char('National id',size = 14)


    # medical
    is_doctor = fields.Boolean(string="Doctor ", default=False, help="If set, the .")
    is_patient = fields.Boolean(string="Patient", default=False, help="If set, the .")

