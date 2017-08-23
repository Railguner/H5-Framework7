# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ws_wharf_parts_record(models.Model):
    _name = 'ws_wharf_parts_record'
    _rec_name = 'uid'

    number = fields.Char(string="记录编号", required=True)
    img = fields.One2many('ws_wharf_parts_img', 'img_id', string="图片")
    time = fields.Datetime(string="时间", required=True)
    local = fields.Char(string="地点", required=True)
    wharf = fields.Many2one('ws_wharf_parts_wharf', string='码头')
    ship = fields.Many2one('ws_wharf_parts_ship', string="船")
    car = fields.Many2one('ws_wharf_parts_car', string="车")
    bulk = fields.Many2one('ws_wharf_parts_bulk', string="散粮堆场")
    place = fields.Many2one('ws_wharf_parts_place', string="仓位")
    to_where = fields.Many2one('ws_wharf_parts_to_where', string="去向")
    uid = fields.Many2one('res.users', string='姓名')

    description = fields.Text(string="描述和评价", required=True)
