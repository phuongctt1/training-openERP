from odoo import api, fields, models

class StudentInformation(models.Model):
    _name = "student.information"
    _description = "student management"
    
    name = fields.Char(string="Họ và tên")
    type= fields.Selection([('male','nam'),('female', 'nữ')],default='male', string='giới tính')
    email= fields.Char(string='Email')
    address = fields.Text(string='Địa chỉ')
    birthday=fields.Date(string="ngày sinh")
    phone=fields.Integer(string="số điện thoại")
    name_one=fields.Char(string="Họ tên bố")
    name_two=fields.Char(string="Họ tên mẹ")
    
    class_id = fields.Many2one("class.information",string="Trường")
    
