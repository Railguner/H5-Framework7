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


class ws_wharf_parts_wharf(models.Model):
    _name = 'ws_wharf_parts_wharf'
    _rec_name = 'wharf_name'

    wharf_name = fields.Char(string='码头', required=True)
    wharf_description = fields.Text(string="描述")

    wharf_id = fields.One2many('ws_wharf_parts_record', 'wharf', string='码头')


class ws_wharf_parts_ship(models.Model):
    _name = 'ws_wharf_parts_ship'
    _rec_name = 'ship_name'

    ship_name = fields.Char(string='船')
    ship_description = fields.Text(string="描述")

    ship_id = fields.One2many('ws_wharf_parts_record', 'ship', string='船')


class ws_wharf_parts_car(models.Model):
    _name = 'ws_wharf_parts_car'
    _rec_name = 'car_name'

    car_name = fields.Char(string='车')
    car_description = fields.Text(string="描述")

    car_id = fields.One2many('ws_wharf_parts_record', 'car', string='车')


class ws_wharf_parts_bulk(models.Model):
    _name = 'ws_wharf_parts_bulk'
    _rec_name = 'bulk_name'

    bulk_name = fields.Char(string='散粮堆场')
    bulk_description = fields.Text(string="描述")

    bulk_id = fields.One2many('ws_wharf_parts_record', 'bulk', string='散粮堆场')


class ws_wharf_parts_place(models.Model):
    _name = 'ws_wharf_parts_place'
    _rec_name = 'place_name'

    place_name = fields.Char(string='仓位')
    place_description = fields.Text(string="描述")

    place_id = fields.One2many('ws_wharf_parts_record', 'place', string='仓位')


class ws_wharf_parts_to_where(models.Model):
    _name = 'ws_wharf_parts_to_where'
    _rec_name = 'to_where_name'

    to_where_name = fields.Char(string='去向')
    to_where_description = fields.Text(string="描述")

    to_where_id = fields.One2many('ws_wharf_parts_record', 'to_where', string='去向')


class ws_wharf_parts_img(models.Model):
    _name = 'ws_wharf_parts_img'
    _rec_name = 'img'

    img_name = fields.Char(string="图片名")
    img = fields.Binary(string='图片', required=True)
    small_img = fields.Binary(string='缩略图')
    img_id = fields.Many2one('ws.wharf.checking', string='图片')


