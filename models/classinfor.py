from odoo import api, fields, models

class ClassInformation(models.Model):
    _name = "class.information"
    _description = "Class Management"
    name = fields.Char(string="Tên lớp")
    grade = fields.Char(string="khối")
    mainTeacher= fields.Char(string="GVCN")
    school_id = fields.Many2one("school.information",string="Trường")