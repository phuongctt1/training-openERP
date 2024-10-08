
from odoo import api, fields, models
class HospitalPatient(models.Model):
    _name = "phuong.patient"
    _description = "Phuong Patient"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),    
    ], required=True, default='male')
    note = fields.Text(string='Description')