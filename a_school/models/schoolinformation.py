from odoo import api, fields, models

class SchoolInformation(models.Model):
    _name = "school.information"
    _description = "school management"
    
    name = fields.Char(string="tên trường")
    type= fields.Selection([('privite','Dân lập'),('public', 'công lập')],default='public', string='loại trường')
    email= fields.Char(string='Email')
    address = fields.Text(string='Địa chỉ')
    phoneNu= fields.Char(string="số điện thoại")
    hasOnlineClass = fields.Boolean(string="có lớp học phụ đạo không")
    rank=fields.Integer(string="Xếp hạng")
    establishDay=fields.Date(string="Ngày thành lập")
    document=fields.Binary(string="Tài liệu về trường")
    document_name= fields.Char(string="tên tài liệu")
    note=fields.Char(string="ghi chú")