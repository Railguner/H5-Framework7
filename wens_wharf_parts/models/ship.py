# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ws_wharf_parts_ship(models.Model):
    _name = 'ws_wharf_parts_ship'
    _rec_name = 'ship_name'

    ship_name = fields.Char(string='船')
    ship_description = fields.Text(string="描述")

    ship_id = fields.One2many('ws_wharf_parts_record', 'ship', string='船')
