from odoo import api, fields, models

class SchoolInformation(models.Model):
    _name = "school.information"
    _description = "School Management"
    
    name = fields.Char(string="tên trường")
    type= fields.Selection([('privite','Dân lập'),('public', 'công lập')],default='public', string='loại trường')
    email= fields.Text(string='Email')
    address = fields.Text(string='Địa chỉ')
    