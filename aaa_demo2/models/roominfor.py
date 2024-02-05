from odoo import api, fields, models

class RoomInfor(models.Model):
    _name = "room.infor"
    _description = "Room Infor"
    
    room_number = fields.Char(string="số phòng", required=True)
    room_type = fields.Selection([
        ('single', 'phòng đơn'),
        ('double', 'phòng đôi'),
        ('family', 'phòng gia đình'),
    ], string="loại phòng", required=True)
    floor = fields.Char(string="số tầng")
    maximunmenber = fields.Integer(string="Giới hạn số người")
    room_image = fields.Binary(string="Ảnh phòng")
    services = fields.Text(string="Mô tả")
    status = fields.Selection([
        ('available', 'Phòng trống'),
        ('booked', 'Phòng đã đặt'),
        ('occupied', 'Phòng đang thuê'),
    ], string="Trạng thái", default='available')

    
