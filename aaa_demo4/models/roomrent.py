from odoo import api, fields, models

class RentInfor(models.Model):
    _name = "room.rent"
    _description = "Room Rent"
    
    name = fields.Char(string="Tên khách hàng")
    identification_card = fields.Char(string="Căn cước công dân")
    check_in_date = fields.Datetime(string="Ngày nhận phòng")
    check_out_date = fields.Datetime(string="Ngày trả phòng")
    room_type = fields.Selection([
        ('single', 'Phòng đơn'),
        ('double', 'Phòng Đôi'),
        ('family', 'Phòng gia đình'),
    ], string="Loại phòng")
    room_number = fields.Char(string="Số phòng")
    room_price = fields.Float(string="Giá phòng/ngày")
    tong= fields.Float(string="Tổng")
    service= fields.Char(string="dịch vụ")
    total_amount = fields.Float(string="Tổng tiền", compute="_compute_total_amount", store=True)
    room_id = fields.Many2one("room.infor",string="Phòng")
    
    @api.depends('check_in_date', 'check_out_date', 'room_price', 'tong')
    def _compute_total_amount(self):
        for record in self:
            # Tính số ngày thuê
            if record.check_in_date and record.check_out_date:
                delta = record.check_out_date - record.check_in_date
                num_of_days = delta.days + 1
            else:
                num_of_days = 0
            
            # Tính tổng tiền
            record.total_amount = (record.room_price * num_of_days) + record.tong
    
