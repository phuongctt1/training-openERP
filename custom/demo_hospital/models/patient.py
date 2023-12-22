from odoo import api, fields, models
class HospitalPatient(models.Model):
    _name = "benhnhan.patient"
    _description = "Benh Nhan Patient"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),    
    ], required=True, default='male')
    note = fields.Text(string='Description')