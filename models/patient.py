from odoo import models, fields, api,_
from datetime import date,datetime
from dateutil.relativedelta import relativedelta


class  patient(models.Model):
    _name = 'abc_hms.patient'
    _description = 'abc_hms.patient'



    #def print_report(self):
        #return self.env.ref('basic_hms.report_print_patient_card').report_action(self)

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

    patient_id = fields.Many2one('res.partner', string="Patient", required=True)
    date_of_birth = fields.Date(string="Date of Birth")
    sex = fields.Selection([('m', 'Male'), ('f', 'Female')], string="Sex")
    age = fields.Char(compute=onchange_age, string="Patient Age", store=True)
    critical_info = fields.Text(string="Patient Critical Information")
    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], string="Blood Type")
    rh = fields.Selection([('-+', '+'), ('--', '-')], string="Rh")
    marital_status = fields.Selection(
        [('s', 'Single'), ('m', 'Married'), ('w', 'Widowed'), ('d', 'Divorced'), ('x', 'Seperated')],
        string='Marital Status')
    deceased = fields.Boolean(string='Deceased')
    date_of_death = fields.Datetime(string="Date of Death")
    cause_of_death = fields.Char(string='Cause of Death')
    current_insurance_id = fields.Many2one('res.partner', string="Insurance")
    partner_address_id = fields.Many2one('res.partner', string="Address", )
    primary_care_physician_id = fields.Many2one('res.partner', domain=[('is_doctor', '=', True)], string="Primary Care Doctor")
    patient_status = fields.Char(string="Hospitalization Status", readonly=True)
    patient_disease_ids = fields.One2many('medical.patient.disease','patient_id')
    #patient_psc_ids = fields.One2many('medical.patient.psc', 'patient_id')
    general_info = fields.Text(string="Info")


    medical_vaccination_ids = fields.One2many('medical.vaccination', 'medical_patient_vaccines_id')
    # medical_appointments_ids = fields.One2many('medical.appointment', 'patient_id', string='Appointments')
    # lastname = fields.Char('Last Name')
    # report_date = fields.Date('Date', default=datetime.today().date())
    # medication_ids = fields.One2many('medical.patient.medication1', 'medical_patient_medication_id')
    # deaths_2nd_week = fields.Integer('Deceased after 2nd week')
    # deaths_1st_week = fields.Integer('Deceased after 1st week')
    # full_term = fields.Integer('Full Term')
    # ses_notes = fields.Text('Notes')


