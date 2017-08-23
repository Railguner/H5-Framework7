# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ws_wharf_parts_car(models.Model):
    _name = 'ws_wharf_parts_car'
    _rec_name = 'car_name'

    car_name = fields.Char(string='车')
    car_description = fields.Text(string="描述")

    car_id = fields.One2many('ws_wharf_parts_record', 'car', string='车')
