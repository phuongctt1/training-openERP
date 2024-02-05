from odoo import api, fields, models

class BookingHotel(models.Model):
    _name = "booking.hotel"
    _description = "Booking Hotel"
    
    customer_name = fields.Char(string='Tên Khách Hàng')
    id_card = fields.Char(string='Căn Cước Công Dân')
    location = fields.Char(string='Địa Điểm Khách Sạn')
    check_in_date = fields.Date(string='Ngày Nhận Phòng')
    check_out_date = fields.Date(string='Ngày Trả Phòng')
    number_of_nights = fields.Integer(string='Số Đêm')
    guests_and_rooms = fields.Char(string='Khách và Phòng')
    roomrent_id = fields.Many2one("room.rent",string="Phòng")
    
