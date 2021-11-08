# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HmsAppointments(models.Model):
    _name = 'abc_hms.appointments'
    _description = 'abc_hms.appointments'

    date = fields.Date()
    doctor_id = fields.Many2one('res.partner', 'Doctor', required=True)
    patient_id = fields.Many2one('res.partner', 'Patient', required=True)
    per = fields.Integer()
