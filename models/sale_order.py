from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'sale.order'

    patient_status = fields.Selection([
        ('ambulatory', 'Ambulatory'),
        ('outpatient', 'Outpatient'),
        ('inpatient', 'Inpatient'),
    ], 'Patient status',  default='outpatient')
    urgency_level = fields.Selection([
        ('a', 'Normal'),
        ('b', 'Urgent'),
        ('c', 'Medical Emergency'),
    ], 'Urgency Level',  default="b")
    invoice_to_insurer = fields.Boolean('Invoice to Insurance')
    insurer_id = fields.Many2one('res.partner', 'Insurer')
    doctor_id = fields.Many2one('res.partner', 'Doctor', required=True)