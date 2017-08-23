# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ws_wharf_parts_place(models.Model):
    _name = 'ws_wharf_parts_place'
    _rec_name = 'place_name'

    place_name = fields.Char(string='仓位')
    place_description = fields.Text(string="描述")

    place_id = fields.One2many('ws_wharf_parts_record', 'place', string='仓位')
