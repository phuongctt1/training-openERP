from odoo import api, models, fields

class HotelStaff(models.Model):
    _name = 'hotel.staff'
    _description = 'Hotel Staff'

    name = fields.Char(string='Tên Nhân Viên')
    position = fields.Selection([
        ('manager', 'Quản Lí'),
        ('employee', 'Nhân Viên')],
        string='Chức Vụ')
    image = fields.Binary(string='Ảnh')
    id_card = fields.Char(string='CMND')
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ')],
        string='Giới Tính')
    phone_number = fields.Char(string='Số Điện Thoại')
    address = fields.Text(string='Địa Chỉ')
    bookinghotel_id = fields.Many2one("booking.hotel",string="Phòng")
    
